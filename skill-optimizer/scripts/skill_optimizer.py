import os, re, json, shutil, argparse
from datetime import datetime
from difflib import SequenceMatcher

SKILLS_DIR = os.environ.get("OPENCLAW_SKILLS_DIR", os.path.expanduser("~/.openclaw/skills"))
DATA_DIR = os.environ.get("OPENCLAW_DATA_DIR", os.path.expanduser("~/.openclaw/workspace_second/data/skill_optimizer"))

ARCHIVE_DIR = os.path.join(SKILLS_DIR, "_archive")

KEYWORD_DOMAIN = {
    "scrape": "Data & Research",
    "crawl": "Data & Research",
    "research": "Data & Research",
    "email": "Comms",
    "notify": "Comms",
    "video": "Media",
    "audio": "Media",
    "image": "Media",
    "security": "Security & Compliance",
    "compliance": "Security & Compliance",
    "automation": "Automation & Ops",
    "deploy": "Dev & Code",
    "code": "Dev & Code",
}

KEYWORD_TASK = {
    "scrape": "Extract",
    "crawl": "Extract",
    "extract": "Extract",
    "analy": "Analyze",
    "summar": "Analyze",
    "convert": "Transform",
    "transform": "Transform",
    "monitor": "Monitor",
    "alert": "Monitor",
    "generate": "Generate",
    "create": "Generate",
    "deploy": "Deploy",
}

KEYWORD_RESOURCE = {
    "api": "API",
    "web": "Web",
    "http": "Web",
    "cli": "CLI",
    "pdf": "Local Files",
    "csv": "Local Files",
    "json": "Local Files",
    "db": "DB",
    "cloud": "Cloud",
}


def ensure_dir(p):
    os.makedirs(p, exist_ok=True)


def backup_skills():
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = os.path.join(DATA_DIR, "backups", ts)
    ensure_dir(dst)
    # Copy skills (excluding archive)
    for name in os.listdir(SKILLS_DIR):
        if name == "_archive":
            continue
        src_path = os.path.join(SKILLS_DIR, name)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, os.path.join(dst, name), dirs_exist_ok=True)
    return dst


def parse_skill_md(path):
    if not os.path.exists(path):
        return {"name": "", "description": "", "body": ""}
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    name = ""
    desc = ""
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2]
            for line in fm.splitlines():
                if line.strip().startswith("name:"):
                    name = line.split("name:", 1)[1].strip()
                if line.strip().startswith("description:"):
                    desc = line.split("description:", 1)[1].strip()
    return {"name": name, "description": desc, "body": body}


def classify(text):
    t = text.lower()
    domains = set()
    tasks = set()
    resources = set()
    for k, v in KEYWORD_DOMAIN.items():
        if k in t:
            domains.add(v)
    for k, v in KEYWORD_TASK.items():
        if k in t:
            tasks.add(v)
    for k, v in KEYWORD_RESOURCE.items():
        if k in t:
            resources.add(v)
    if not domains:
        domains.add("Automation & Ops")
    if not tasks:
        tasks.add("Analyze")
    if not resources:
        resources.add("Local Files")
    return sorted(domains), sorted(tasks), sorted(resources)


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def build_index(skills):
    idx = []
    for s in skills:
        idx.append({
            "skill_id": s["id"],
            "name": s["meta"]["name"] or s["id"],
            "description": s["meta"]["description"],
            "domains": s["domains"],
            "task_types": s["tasks"],
            "resource_types": s["resources"],
            "path": s["path"],
            "updated_at": datetime.now().strftime("%Y-%m-%d"),
        })
    return idx


def write_json(path, obj):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def write_text(path, text):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--deep-pass", type=int, default=2)
    args = ap.parse_args()

    ensure_dir(DATA_DIR)
    backup_path = backup_skills()

    skills = []
    for name in os.listdir(SKILLS_DIR):
        if name == "_archive":
            continue
        skill_dir = os.path.join(SKILLS_DIR, name)
        if not os.path.isdir(skill_dir):
            continue
        meta = parse_skill_md(os.path.join(skill_dir, "SKILL.md"))
        combined = f"{meta.get('name','')} {meta.get('description','')} {meta.get('body','')}"
        domains, tasks, resources = classify(combined)
        skills.append({
            "id": name,
            "path": skill_dir,
            "meta": meta,
            "domains": domains,
            "tasks": tasks,
            "resources": resources,
            "combined": combined,
        })

    # duplicates
    duplicates = []
    for i in range(len(skills)):
        for j in range(i + 1, len(skills)):
            a = skills[i]
            b = skills[j]
            score = similarity(a["combined"], b["combined"])
            if score >= 0.90:
                duplicates.append({
                    "a": a["id"],
                    "b": b["id"],
                    "score": round(score, 3)
                })

    # build merge candidates report
    report_lines = ["# Merge candidates", ""]
    for d in duplicates:
        report_lines.append(f"- {d['a']}  <->  {d['b']}  (score={d['score']})")
    report = "\n".join(report_lines)

    # apply merges (archive duplicates)
    if args.apply:
        month = datetime.now().strftime("%Y-%m")
        archive_month = os.path.join(ARCHIVE_DIR, month)
        ensure_dir(archive_month)
        for d in duplicates:
            a = next(s for s in skills if s["id"] == d["a"])
            b = next(s for s in skills if s["id"] == d["b"])
            # choose primary by longer description
            primary = a if len(a["meta"].get("description", "")) >= len(b["meta"].get("description", "")) else b
            duplicate = b if primary is a else a
            src = duplicate["path"]
            dst = os.path.join(archive_month, duplicate["id"])
            if os.path.exists(src) and not os.path.exists(dst):
                shutil.move(src, dst)

    # index
    index = build_index(skills)

    # memory summary (deep-pass)
    memory_lines = [f"# Skill memory summary ({datetime.now().isoformat()})", ""]
    for _ in range(max(1, args.deep_pass)):
        for s in skills:
            memory_lines.append(f"- {s['id']}: {s['meta'].get('description','')}")
        memory_lines.append("")

    # write outputs
    write_json(os.path.join(DATA_DIR, "artifacts", "scan", "skills.json"), skills)
    write_json(os.path.join(DATA_DIR, "artifacts", "dedupe", "duplicates.json"), duplicates)
    write_text(os.path.join(DATA_DIR, "artifacts", "dedupe", "merge_candidates.md"), report)
    write_json(os.path.join(DATA_DIR, "index", "skills_index.json"), index)
    write_text(os.path.join(DATA_DIR, "index", "skills_index.md"), "\n".join([f"- {i['skill_id']}: {i['description']}" for i in index]))
    write_text(os.path.join(DATA_DIR, "memory", "skills_memory.md"), "\n".join(memory_lines))
    write_text(os.path.join(DATA_DIR, "last_backup.txt"), backup_path)


if __name__ == "__main__":
    main()
