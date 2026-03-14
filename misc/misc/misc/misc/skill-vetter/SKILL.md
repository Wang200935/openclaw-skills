---
name: skill-vetter
description: Review third-party or newly created skills for safety, scope, overlap, and operational risk before installation or activation. Use when evaluating external skills from ClawHub or local folders, checking whether a skill requests risky behavior, duplicates existing capability, or should be installed, rejected, or sandbox-reviewed first.
---

# Skill Vetter

Use this skill before trusting a new skill.

## Review checklist

1. Check what problem the skill claims to solve.
2. Check whether existing local skills already cover the need.
3. Look for dangerous patterns:
   - destructive commands
   - silent external calls
   - credential handling
   - eval / arbitrary code execution
   - hidden installs or side effects
4. Decide one of:
   - install now
   - install only after manual review
   - skip because redundant
   - reject because risky

## Output format

- Candidate skill
- Claimed value
- Overlap with existing stack
- Main risks
- Install recommendation



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\misc\skill-vetter\SKILL.md
---
---
name: skill-vetter
version: 1.0.0
description: Security-first skill vetting for AI agents. Use before installing any skill from ClawdHub, GitHub, or other sources. Checks for red flags, permission scope, and suspicious patterns.
---

# Skill Vetter ??

Security-first vetting protocol for AI agent skills. **Never install a skill without vetting it first.**

## When to Use

- Before installing any skill from ClawdHub
- Before running skills from GitHub repos
- When evaluating skills shared by other agents
- Anytime you're asked to install unknown code

## Vetting Protocol

### Step 1: Source Check

```
Questions to answer:
- [ ] Where did this skill come from?
- [ ] Is the author known/reputable?
- [ ] How many downloads/stars does it have?
- [ ] When was it last updated?
- [ ] Are there reviews from other agents?
```

### Step 2: Code Review (MANDATORY)

Read ALL files in the skill. Check for these **RED FLAGS**:

```
?ö® REJECT IMMEDIATELY IF YOU SEE:
?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä
??curl/wget to unknown URLs
??Sends data to external servers
??Requests credentials/tokens/API keys
??Reads ~/.ssh, ~/.aws, ~/.config without clear reason
??Accesses MEMORY.md, USER.md, SOUL.md, IDENTITY.md
??Uses base64 decode on anything
??Uses eval() or exec() with external input
??Modifies system files outside workspace
??Installs packages without listing them
??Network calls to IPs instead of domains
??Obfuscated code (compressed, encoded, minified)
??Requests elevated/sudo permissions
??Accesses browser cookies/sessions
??Touches credential files
?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä
```

### Step 3: Permission Scope

```
Evaluate:
- [ ] What files does it need to read?
- [ ] What files does it need to write?
- [ ] What commands does it run?
- [ ] Does it need network access? To where?
- [ ] Is the scope minimal for its stated purpose?
```

### Step 4: Risk Classification

| Risk Level | Examples | Action |
|------------|----------|--------|
| ?ü¢ LOW | Notes, weather, formatting | Basic review, install OK |
| ?ü° MEDIUM | File ops, browser, APIs | Full code review required |
| ?î¥ HIGH | Credentials, trading, system | Human approval required |
| ??EXTREME | Security configs, root access | Do NOT install |

## Output Format

After vetting, produce this report:

```
SKILL VETTING REPORT
?ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚???Skill: [name]
Source: [ClawdHub / GitHub / other]
Author: [username]
Version: [version]
?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä
METRICS:
??Downloads/Stars: [count]
??Last Updated: [date]
??Files Reviewed: [count]
?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä
RED FLAGS: [None / List them]

PERMISSIONS NEEDED:
??Files: [list or "None"]
??Network: [list or "None"]  
??Commands: [list or "None"]
?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä?Ä
RISK LEVEL: [?ü¢ LOW / ?ü° MEDIUM / ?î¥ HIGH / ??EXTREME]

VERDICT: [??SAFE TO INSTALL / ?†Ô? INSTALL WITH CAUTION / ??DO NOT INSTALL]

NOTES: [Any observations]
?ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚??ê‚???```

## Quick Vet Commands

For GitHub-hosted skills:
```bash
# Check repo stats
curl -s "https://api.github.com/repos/OWNER/REPO" | jq '{stars: .stargazers_count, forks: .forks_count, updated: .updated_at}'

# List skill files
curl -s "https://api.github.com/repos/OWNER/REPO/contents/skills/SKILL_NAME" | jq '.[].name'

# Fetch and review SKILL.md
curl -s "https://raw.githubusercontent.com/OWNER/REPO/main/skills/SKILL_NAME/SKILL.md"
```

## Trust Hierarchy

1. **Official OpenClaw skills** ??Lower scrutiny (still review)
2. **High-star repos (1000+)** ??Moderate scrutiny
3. **Known authors** ??Moderate scrutiny
4. **New/unknown sources** ??Maximum scrutiny
5. **Skills requesting credentials** ??Human approval always

## Remember

- No skill is worth compromising security
- When in doubt, don't install
- Ask your human for high-risk decisions
- Document what you vet for future reference

---

*Paranoia is a feature.* ????




