# Page 131 - Impostazione del Problema Dinamico

## Impostazione del Problema Dinamico

L'equazione della dinamica che avevamo trovato è

$$[M]\{\ddot{q}\} = \{r\} + \{\hat{f}\}$$

ma poco fa abbiamo trovato che $\{r\} = -[\Psi_q]^T\{\lambda\}$, quindi:

$$\boxed{[M]\{\ddot{q}\} + [\Psi_q]^T\{\lambda\} = \{\hat{f}\}}$$

$\{\hat{f}\}$ = componenti lagrangiane delle sollecitazioni lungo i movimenti virtuali.

Supponendo i vincoli privi di attrito, bilaterali e indipendenti dal tempo esterno:

$$\{\Psi\} = \{0\} \xrightarrow{\text{derivando}} [\Psi_q]\{\dot{q}\} = \{0\} \xrightarrow{\text{derivando}} [\Psi_q]\{\ddot{q}\} = \{\delta\}, \text{ con } \{\delta\} = -\{([\Psi_q]\{\dot{q}\}),_q\}\{\dot{q}\}$$

quindi mettendo a sistema l'equazione della dinamica ed il vincolo sulle accelerazioni:

$$\begin{cases} [M]\{\ddot{q}\} + [\Psi_q]^T\{\lambda\} = \{\hat{f}\} \\ [\Psi_q]\{\ddot{q}\} = \{\delta\} \end{cases}$$

con le dimensioni:
- $[M]$: $m \times m$, $\{\ddot{q}\}$: $m$, $[\Psi_q]^T$: $m \times p$, $\{\lambda\}$: $p$, $\{\hat{f}\}$: $m$
- $[\Psi_q]$: $p \times m$, $\{\ddot{q}\}$: $m$, $\{\delta\}$: $p$

Fissato un istante "$t$", in cui conosciamo $\{q\}$ e $\{\dot{q}\}$, si possono ricavare le equazioni di vincolo $\{\Psi_q\}$ in cui le incognite sono le $\{\ddot{q}\}$. Nella prima equazione, invece, le incognite sono le $\{\lambda\}$, per cui ho $m + p$ incognite.

È possibile assemblare il sistema in un'unica equazione matriciale.

$$\begin{bmatrix} [M] & [\Psi_q]^T \\ [\Psi_q] & [0] \end{bmatrix} \begin{Bmatrix} \{\ddot{q}\} \\ \{\lambda\} \end{Bmatrix} = \begin{Bmatrix} \{\hat{f}\} \\ \{\delta\} \end{Bmatrix} \implies \boxed{[A]\{x\} = \{b\}}$$

con dimensioni: $[A]$: $(p+m) \times (p+m)$, $\{x\}$: $p+m$, $\{b\}$: $p+m$

Si è ottenuto un sistema lineare di incognite $\{x\}$, risolvibile nel modo classico:

$$\{x\} = [A]^{-1}\{b\}$$

per cui è possibile calcolare le accelerazioni e i moltiplicatori di Lagrange (vettore $\{\lambda\}$) ad un generico istante del tempo; grazie alle $\{\lambda\}$ si possono calcolare le reazioni vincolari, mentre grazie alle $\{\ddot{q}\}$ si possono calcolare velocità e posizioni all'istante successivo.

Usiamo l'**INTEGRAZIONE PASSO-PASSO**: all'istante $t_i$ conosco $\{q\}_i$ e $\{\dot{q}\}_i$ $\Rightarrow$ conosco anche i termini $[\Psi_{q,i}]$, $[\Psi_{q,i}]$, $\{\delta\}_i$; grazie ai quali sono risolvere il sistema $\{x\} = [A]^{-1}\{b\}$.

Da esso ricavo $\{\ddot{q}\}_i$, da cui ottengo $\{\dot{q}\}_{i+1} = \{\dot{q}\}_i + \{\ddot{q}\}_i \Delta t$ e $\{q\}_{i+1} = \{q\}_i + \{\dot{q}\}_i \Delta t$, e $\{\lambda\}_i$

con cui ricavo $\{r\}_{i} = +[\Psi_q]^T_i \{\lambda\}_i$. Si procede analogamente all'istante $t_{i+1}$.
