import random

def generate_research_topic_prompt():
    areas = [
    # Activation Functions
    "activation function design for deep neural networks",
    "gated activation functions in transformers",
    "trainability and gradient flow of activation functions",
    "normalization-aware activation functions",
    "sparse and efficient activation functions",

    # Loss Functions
    "loss function design for deep learning",
    "contrastive and non-contrastive loss functions",
    "robust loss functions under label noise",
    "calibration-aware loss functions",
    "sequence-level loss functions for language models",

    # Classical Machine Learning
    "ensemble methods in classical machine learning",
    "kernel methods for large-scale machine learning",
    "probabilistic graphical models",
    "bayesian nonparametric machine learning",
    "generalization bounds in machine learning",
    "model interpretability theory",
    "causal inference with machine learning",

    # Deep Learning Architectures
    "efficient attention mechanisms",
    "sparse neural network architectures",
    "mixture of experts neural networks",
    "neural scaling laws",
    "depth versus width trade-offs in deep learning",
    "training dynamics of deep neural networks",
    "initialization strategies for deep networks",
    "normalization layers in transformers",
    "curriculum learning in deep learning",
    "emergent behaviors in deep neural networks",

    # NLP (General)
    "sequence to sequence architectures for NLP",
    "tokenization and subword modeling",
    "long context modeling in NLP",
    "multilingual neural machine translation",
    "low resource NLP methods",
    "evaluation metrics for NLP models",
    "robustness and distribution shift in NLP",
    "benchmark saturation in NLP",

    # Reinforcement Learning
    "policy optimization methods in reinforcement learning",
    "value based reinforcement learning improvements",
    "model based reinforcement learning",
    "offline reinforcement learning",
    "multi agent reinforcement learning",
    "reinforcement learning for sequence modeling",
    "reinforcement learning from human feedback",
    "exploration strategies in deep reinforcement learning",
    "credit assignment in reinforcement learning",

    # Large Language Models
    "transformer architecture alternatives",
    "grouped query and multi query attention",
    "long context large language models",
    "sparse attention for large language models",
    "retrieval augmented generation architectures",
    "pretraining objectives for large language models",
    "instruction tuning methods",
    "alignment and preference learning objectives",
    "data quality versus scale in language model training",

    # LLM Inference & Serving
    "large language model inference optimization",
    "key value cache optimization",
    "speculative decoding for language models",
    "quantization methods for large language models",
    "batching strategies for language model serving",
    "latency throughput trade-offs in model serving",

    # CPU / GPU / Systems Optimization
    "gpu memory optimization for deep learning",
    "distributed training of large neural networks",
    "zero redundancy and fsdp training methods",
    "gradient checkpointing techniques",
    "communication efficient distributed training",
    "mixed precision training techniques",
    "cpu gpu offloading for neural networks",
    "edge inference optimization",

    # AI Systems & Design
    "machine learning system design",
    "end to end ml pipelines",
    "model lifecycle management",
    "model monitoring and data drift detection",
    "reproducibility in machine learning systems",
    "failure modes of ai systems",
    "cost efficient machine learning systems",
    "fairness and bias mitigation in machine learning",
    "system level evaluation of ai models",
    "ai systems in production case studies"
    ]

    sampled_area = random.choice(areas)

    prompt = f"""
    Suggest one focused yet sufficiently broad research topic suitable for discovering multiple
    high-quality research papers via academic search.

    The topic MUST be centered around the following research area:
    {sampled_area}

    The topic should be interesting, non-trivial, and research-relevant, with enough depth and scope
    to have multiple influential or recent papers. Return only the topic as a short phrase.

    DO NOT OUTPUT ANY OTHER ADDITIONAL TEXT APART FROM THE TOPIC.
    """.strip()
    return prompt



def generate_paper_analysis_prompt(paper_content): 
    prompt = f""" You are given the content of a research paper (may include title, abstract, introduction, or full text). Analyze it and return ONLY a valid JSON object with the following keys:
    
    {{
        "paper_title": "Extract the exact paper title as mentioned in the content (string). If not found, use null.",
        "paper_summary": "A lucid, digestible summary (5–8 sentences) explaining what the paper is about, what is good/novel about it, and its implications. Be interesting but not overly detailed.",
        "relevance": "Why this paper matters and what future scope/directions it opens (3–5 sentences).",
        "related_topics": ["2–3 closely related research topics or keywords (strings)."]
        }}
        
    Rules: 
    - Output JSON only (no markdown, no commentary). 
    - Keep the summary accessible but technically accurate. 
    - Do not hallucinate details not present in the content; if uncertain, say  so briefly in the relevant field. 
    - related_topics must have 2–3 items maximum. 
    
    PAPER CONTENT: {paper_content}""".strip() 
    return prompt
