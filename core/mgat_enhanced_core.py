# “””
Multi-Geometric Attention Theory (MGAT) - Core Demonstration

Minimal implementation showing how different geometric attention patterns
produce distinct representational states, supporting the theory that
attention acts as a measurement operator.

Author: Hillary Danan
Framework: https://github.com/HillaryDanan/multi-geometric-attention
“””

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Tuple, Optional
from dataclasses import dataclass
import warnings
warnings.filterwarnings(‘ignore’)

# ============================================================================

# CORE GEOMETRIC PATTERNS

# ============================================================================

@dataclass
class AttentionGeometry:
“”“Defines a geometric attention pattern and its properties”””
name: str
pattern_matrix: np.ndarray
entropy: float
connectivity: float

class GeometricAttention:
“””
Core MGAT implementation: Different geometric patterns of attention
transform neural representations into distinct conscious states
“””

```
def __init__(self, dim: int = 8):
    self.dim = dim
    self.patterns = self._initialize_patterns()
    
def _initialize_patterns(self) -> Dict[str, np.ndarray]:
    """Initialize the four fundamental geometric attention patterns"""
    
    patterns = {}
    
    # 1. Sequential/Square Pattern (focused, linear processing)
    sequential = np.zeros((self.dim, self.dim))
    for i in range(self.dim):
        for j in range(max(0, i-1), min(self.dim, i+2)):
            sequential[i, j] = 1.0 / (1 + abs(i - j))
    patterns['sequential'] = sequential / sequential.sum(axis=1, keepdims=True)
    
    # 2. Associative/Hexagonal Pattern (memory, pattern completion)
    associative = np.ones((self.dim, self.dim))
    for i in range(self.dim):
        for j in range(self.dim):
            dist = min(abs(i - j), self.dim - abs(i - j))  # Circular distance
            associative[i, j] = np.exp(-0.5 * (dist / 2) ** 2)
    patterns['associative'] = associative / associative.sum(axis=1, keepdims=True)
    
    # 3. Hierarchical/Triangular Pattern (abstraction, categorization)
    hierarchical = np.zeros((self.dim, self.dim))
    for i in range(self.dim):
        for j in range(i + 1):
            hierarchical[i, j] = 1.0 / (i + 1)
    patterns['hierarchical'] = hierarchical / (hierarchical.sum(axis=1, keepdims=True) + 1e-8)
    
    # 4. Creative/Aperiodic Pattern (novel connections, insight)
    np.random.seed(42)  # For reproducibility
    creative = np.random.rand(self.dim, self.dim)
    creative = (creative + creative.T) / 2  # Symmetrize
    creative = np.exp(creative) / np.exp(creative).sum(axis=1, keepdims=True)
    patterns['creative'] = creative
    
    return patterns

def measure(self, neural_state: np.ndarray, geometry: str) -> np.ndarray:
    """
    Apply geometric attention as measurement operator
    Transforms probabilistic neural state into conscious representation
    """
    if geometry not in self.patterns:
        raise ValueError(f"Unknown geometry: {geometry}")
        
    attention_matrix = self.patterns[geometry]
    
    # Attention as measurement: A|ψ⟩ = |φ⟩
    measured_state = attention_matrix @ neural_state
    
    # Normalize (collapse to measured state)
    measured_state = measured_state / (np.linalg.norm(measured_state) + 1e-8)
    
    return measured_state

def compute_entropy(self, pattern: np.ndarray) -> float:
    """Calculate Shannon entropy of attention pattern"""
    flat = pattern.flatten()
    flat = flat[flat > 0]
    return -np.sum(flat * np.log2(flat + 1e-10))

def compute_connectivity(self, pattern: np.ndarray) -> float:
    """Calculate connectivity measure of pattern"""
    return np.sum(pattern > 0.01) / pattern.size
```

# ============================================================================

# DEMONSTRATION: STATE TRANSFORMATIONS

# ============================================================================

def demonstrate_geometric_transformations():
“””
Show how different geometric attention patterns transform the same
initial neural state into distinct conscious representations
“””

```
# Initialize system
attention = GeometricAttention(dim=16)

# Create initial neural state (superposition of features)
np.random.seed(123)
initial_state = np.random.randn(16)
initial_state = initial_state / np.linalg.norm(initial_state)

# Apply different geometric measurements
results = {}
for geometry in ['sequential', 'associative', 'hierarchical', 'creative']:
    measured = attention.measure(initial_state, geometry)
    entropy = attention.compute_entropy(attention.patterns[geometry])
    connectivity = attention.compute_connectivity(attention.patterns[geometry])
    
    results[geometry] = {
        'state': measured,
        'entropy': entropy,
        'connectivity': connectivity,
        'pattern': attention.patterns[geometry]
    }

# Visualize transformations
fig, axes = plt.subplots(2, 4, figsize=(16, 8))

for idx, (name, data) in enumerate(results.items()):
    # Plot attention pattern
    ax1 = axes[0, idx]
    im = ax1.imshow(data['pattern'], cmap='viridis', aspect='auto')
    ax1.set_title(f'{name.capitalize()} Pattern\nH={data["entropy"]:.2f}, C={data["connectivity"]:.2f}')
    ax1.set_xlabel('Input Dimension')
    ax1.set_ylabel('Output Dimension')
    plt.colorbar(im, ax=ax1, fraction=0.046)
    
    # Plot resulting state
    ax2 = axes[1, idx]
    ax2.bar(range(len(data['state'])), data['state'])
    ax2.set_title(f'Measured State')
    ax2.set_xlabel('Feature')
    ax2.set_ylabel('Activation')
    ax2.set_ylim([-0.5, 0.5])

plt.suptitle('MGAT: Geometric Attention as Measurement Operator', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

return results
```

# ============================================================================

# DEMONSTRATION: DYNAMIC TRANSITIONS

# ============================================================================

def demonstrate_attention_dynamics():
“””
Show how attention can transition between geometric modes,
modeling shifts in conscious states (focus -> creativity -> memory)
“””

```
attention = GeometricAttention(dim=12)
timesteps = 100

# Define attention mode sequence (simulating cognitive task)
mode_sequence = (
    ['sequential'] * 25 +      # Initial focus
    ['creative'] * 25 +         # Insight generation  
    ['associative'] * 25 +      # Memory consolidation
    ['hierarchical'] * 25       # Abstraction
)

# Initialize state
state = np.random.randn(12)
state = state / np.linalg.norm(state)

# Track evolution
states = []
entropies = []

for t in range(timesteps):
    mode = mode_sequence[t]
    state = attention.measure(state, mode)
    states.append(state.copy())
    entropies.append(attention.compute_entropy(attention.patterns[mode]))

# Visualize dynamics
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# State evolution heatmap
states_matrix = np.array(states).T
im1 = ax1.imshow(states_matrix, cmap='RdBu_r', aspect='auto', vmin=-0.5, vmax=0.5)
ax1.set_title('Neural State Evolution Under Geometric Attention Transitions')
ax1.set_xlabel('Time')
ax1.set_ylabel('Neural Dimension')
plt.colorbar(im1, ax=ax1)

# Add mode boundaries
for boundary in [25, 50, 75]:
    ax1.axvline(x=boundary, color='black', linestyle='--', alpha=0.5)

# Entropy over time
ax2.plot(entropies, linewidth=2)
ax2.set_title('Attention Entropy (Information Capacity)')
ax2.set_xlabel('Time')
ax2.set_ylabel('Entropy')
ax2.grid(True, alpha=0.3)

# Add mode labels
mode_labels = ['Sequential', 'Creative', 'Associative', 'Hierarchical']
for i, label in enumerate(mode_labels):
    ax2.text(12.5 + i*25, max(entropies)*0.9, label, ha='center')

plt.tight_layout()
plt.show()

return states_matrix
```

# ============================================================================

# MAIN EXECUTION

# ============================================================================

if **name** == “**main**”:
print(”=” * 70)
print(“MULTI-GEOMETRIC ATTENTION THEORY - CORE DEMONSTRATION”)
print(”=” * 70)
print(”\nDemonstrating how attention geometry shapes conscious states…”)
print(”-” * 70)

```
# Run demonstrations
print("\n1. GEOMETRIC TRANSFORMATIONS")
print("   Showing how different attention patterns transform neural states")
transformation_results = demonstrate_geometric_transformations()

print("\n2. ATTENTION DYNAMICS") 
print("   Modeling transitions between attention modes over time")
dynamics_results = demonstrate_attention_dynamics()

print("\n" + "=" * 70)
print("KEY INSIGHTS:")
print("-" * 70)
print("• Each geometric pattern produces distinct state transformations")
print("• Sequential attention: Low entropy, focused processing")
print("• Creative attention: High entropy, novel connections")
print("• Associative attention: Distributed, memory-like")
print("• Hierarchical attention: Structured, abstraction")
print("\nThis supports MGAT's core claim that attention geometry")
print("determines the structure of conscious experience.")
print("=" * 70)
```
