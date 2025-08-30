# Cross-Linguistic Attention Dynamics: A Framework for Empirical Investigation

## Abstract

This paper proposes empirically testable hypotheses about how orthographic properties might influence attention patterns in transformer models. We explicitly avoid causal claims, focusing instead on measurable correlations that could inform future controlled experiments. Building from observed phase distributions in language model outputs (9.7% transformation phase in GPT-3.5), we propose methods to investigate whether linguistic properties correlate with measurable attention dynamics.

## 1. Background

### 1.1 What We Know

- Transformer attention mechanisms vary across layers and tasks (Clark et al., 2019)
- Multilingual models process different languages through shared representations (Pires et al., 2019)
- Orthographic depth affects human reading processes (Frost et al., 1987; Katz & Frost, 1992)
- GPT-3.5 shows distinct response phases: 9.7% transformation, varying rates of analysis/synthesis (preliminary observation requiring replication)

### 1.2 What We Don't Know

- Whether orthographic properties correlate with attention patterns
- If such correlations exist, what mechanisms might explain them
- Whether observed phase distributions relate to attention dynamics

## 2. Testable Hypotheses

### 2.1 Attention Entropy Across Languages

**Hypothesis 1**: Attention entropy will correlate with orthographic depth.

**Operational definitions**:
- Attention entropy: H = -Σ p(i,j) log p(i,j) for attention weights
- Orthographic depth: Established measure from psycholinguistics (Katz & Frost, 1992)

**Measurement**:
1. Extract attention matrices for identical semantic content across languages
2. Calculate entropy per layer
3. Correlate with orthographic depth scores

**Confounds to control**:
- Syntactic complexity
- Morphological richness  
- Training data frequency
- Tokenization differences

### 2.2 Layer-wise Attention Stability

**Hypothesis 2**: Attention patterns show increasing stability (decreasing variance) in deeper layers.

**Operational definition**:
- Stability: 1 - std(attention_weights) across similar inputs

**Measurement**:
1. Present paraphrases of same content
2. Measure attention weight variance per layer
3. Compare progression across languages

**This tests processing commitment, not "reversibility"**

### 2.3 Phase Distribution and Attention Patterns

**Hypothesis 3**: Response phase correlates with measurable attention characteristics.

**Building from Ouroboros findings**:
- Transformation phase (9.7%): Novel recombination
- Analysis phase: Decomposition
- Synthesis phase: Integration

**Measurement**:
1. Classify responses into phases (using existing criteria)
2. Extract attention patterns for each phase
3. Identify characteristic attention signatures

**Not claiming causation, only correlation**

## 3. Experimental Design

### 3.1 Controlling for Confounds

**Matched stimuli across languages**:
- Use translation-equivalent sentences
- Control for length, complexity, semantic content
- Include multiple domains (narrative, factual, instructional)

**Statistical controls**:
- Multilevel modeling to account for language families
- Control for training data proportions
- Include tokenization metrics as covariates

### 3.2 Power Analysis and Sample Size Considerations

**Minimum Detectable Effect Size**: 
With 3-5 languages and multiple confounds, detecting correlations requires large effect sizes (r > 0.7) for 80% power. This pilot deliberately targets only strong correlations.

**Sample Size Justification**:
- Pilot phase (3-5 languages): Detect only large effects, establish feasibility
- Validation phase (10-15 languages): Medium effects (r > 0.4) detectable
- Full study (30+ languages): Small-medium effects (r > 0.25) with confound controls

**Statistical Power Limitations**:
- With 5 languages and 3 covariates: Power = 0.31 for r = 0.5
- Need 20 languages for 80% power to detect r = 0.5 with controls
- Pilot explicitly exploratory, not confirmatory

### 3.3 What We're NOT Claiming

- That orthography CAUSES attention patterns
- That biological concepts apply to transformers
- That attention patterns have "geometric" shapes
- That models can "reverse" cognitive processes

### 3.4 Incremental Validation

**Stage 1**: Establish whether attention patterns differ systematically across languages
**Stage 2**: If differences exist, identify which linguistic features correlate
**Stage 3**: Design controlled experiments to test specific mechanisms

## 4. Limitations

### 4.1 Correlation vs Causation

Even strong correlations between orthographic properties and attention patterns would not establish causation. Alternative explanations include:
- Training data artifacts
- Correlated linguistic features
- Model architecture biases
- Tokenization effects

### 4.2 Measurement Challenges

- Attention weights may not reflect actual information flow (Jain & Wallace, 2019)
- Layer-wise analysis assumes comparable functions across layers
- Phase classification requires subjective judgment

### 4.3 Generalization Limits

- Findings from one model family may not generalize
- Language-specific patterns might reflect training, not processing
- Results may be task-dependent

## 5. Value Proposition

### 5.1 Why This Matters

If orthographic properties correlate with attention dynamics:
- Could inform multilingual model design
- Might explain performance variations across languages
- Could guide prompt engineering strategies

### 5.2 Incremental Contribution

This framework:
- Provides testable hypotheses about attention dynamics
- Connects established psycholinguistic concepts to NLP
- Offers measurable metrics for cross-linguistic comparison

## 6. Next Steps

1. **Pilot study**: Test hypothesis 1 with 3-5 languages varying in orthographic depth
2. **Replication**: Verify phase distributions across multiple models
3. **Refinement**: Adjust metrics based on pilot results
4. **Scaling**: If patterns emerge, expand to larger language sample

## References

- Clark, K., et al. (2019). "What does BERT look at? An analysis of BERT's attention." ACL.
- Frost, R., Katz, L., & Bentin, S. (1987). "Strategies for visual word recognition." Journal of Experimental Psychology, 13(1), 104-115.
- Jain, S., & Wallace, B. C. (2019). "Attention is not explanation." NAACL.
- Katz, L., & Frost, R. (1992). "The orthographic depth hypothesis." Haskins Laboratories Status Report, 71-102.
- Pires, T., et al. (2019). "How multilingual is multilingual BERT?" ACL.

---

*Note: This framework proposes correlational studies, not causal claims. The 9.7% transformation phase observation requires peer review. All hypotheses require empirical validation before any conclusions can be drawn.*
