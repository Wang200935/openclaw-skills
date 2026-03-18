# Jina config notes

Typical embedding config:
- provider: `openai-compatible`
- model: `jina-embeddings-v5-text-small`
- baseURL: `https://api.jina.ai/v1`
- dimensions: `1024`
- taskQuery: `retrieval.query`
- taskPassage: `retrieval.passage`
- normalized: `true`

Typical rerank config:
- rerank: `cross-encoder`
- rerankProvider: `jina`
- rerankModel: `jina-reranker-v3`
- rerankEndpoint: `https://api.jina.ai/v1/rerank`
