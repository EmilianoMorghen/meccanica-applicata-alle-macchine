# Page 18 - Teorema del Dini e Forme Critiche

Questa matrice ha dimensione $P \times M$, e quindi è rettangolare: se le P equazioni di vincolo devono essere indipendenti, questa matrice dovrà essere a rango massimo.

Innanzitutto dovremo ordinare i parametri in modo che le prime "P" coordinate siano proprio le variabili dipendenti "$u$"; mentre le restanti $M - P$ coordinate, siano proprio le "F" coordinate indipendenti "$\mathit{NS}$". Così si divide la matrice Jacobiana in due sottomatrici:

$$[\Psi_q]_{P \times M} = \left[ [\Psi_u]_{P \times P} \mid [\Psi_{\mathit{NS}}]_{P \times F} \right]$$

Ovviamente questa matrice dipenderà da quali parametri indipendenti si scelgono per descrivere il sistema (nel caso del manovellismo, dipende se uso $\vartheta_2$, $\vartheta_3$ oppure $S$).

Vediamo nel manovellismo: supponendo che sia la manovella a muoversi, avrei

$$\underset{\text{INDIPENDENTI}}{\{NS\}} = \{\vartheta_2\} \quad ; \quad \underset{\text{DIPENDENTI}}{\{u\}} = \{\vartheta_3, S\}^T$$

supponendo, invece, che sia lo stantuffo a muoversi: $\{NS\} = \{S\}$ ; $\{u\} = \{\vartheta_2, \vartheta_3\}^T$

e quindi la matrice Jacobiana andrà riordinata a seconda del set di equazioni scelto per descrivere il sistema.

---

A questo punto devono essere verificate le **IPOTESI DI APPLICAZIONE DEL TEOREMA DEL DINI**:

**①** $\{\hat{q}\} = \begin{Bmatrix} \{\hat{u}\} \\ \{\hat{\mathit{NS}}\} \end{Bmatrix}$ è una soluzione (supponiamo la esista una soluzione per il meccanismo);

**②** le $\{\Psi_q\}$ sono funzioni continue;

**③** le $\frac{\partial \Psi}{\partial q}$ (derivate parziali) sono continue nell'intorno della soluzione $\{\hat{q}\}$;

**④** $\det(\Psi_u) \neq 0$ dove $\Psi_u$ è la sottomatrice delle variabili dipendenti.

Qualora queste ipotesi siano verificate, allora per il teorema del Dini: "esiste almeno $u$ — una soluzione, sotto forma di un set di equazioni $u(NS)$, tali che $\{u(\hat{\mathit{NS}})\} = \{\hat{u}\}^T$

E siccome $u(NS)$ sono delle funzioni esplicite, allora si può risolvere il problema!

---

Nel caso in cui $\boxed{\det(\Psi_u) = 0}$, si ha la **FORMA CRITICA**, che può essere di 2 tipologie:

1. **FORMA CRITICA ISTANTANEA**, in cui $\det(\Psi_u) = 0$ solo nell'intorno di $\hat{q}$;
2. **FORMA CRITICA PERMANENTE**, in cui $\det(\Psi_u) = 0$ sempre.
