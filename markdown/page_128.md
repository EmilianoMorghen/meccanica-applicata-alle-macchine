# Page 128 - Equazioni della Dinamica per N corpi (Matrice di Massa)

Con queste espressioni si può riscrivere il sistema come:

$$\begin{cases} [m_j]_{3 \times 3} \{\ddot{q}_j\}_3 = \{f_j\}_3 + \{r_j\}_3 \\ j = 1, \ldots, N \end{cases}$$

questa equazione comprende entrambe quelle della dinamica.

Questo sistema di equazioni può essere scritto per ogni corpo presente nel sistema; per cui se ho un sistema con N corpi, ho anche **COORDINATE LAGRANGIANE** $\boxed{M = 3N}$

Usando il free-body, è possibile disaccoppiare le equazioni; ma allo stesso modo esse possono essere scritte tutte insieme usando la **MATRICE** $[M]$:

$$[M]_{m \times m} = \begin{bmatrix} [m_1] & [\phi] & \cdots & [\phi] \\ [\phi] & [m_2] & \cdots & [\phi] \\ \vdots & \vdots & \ddots & \vdots \\ [\phi] & [\phi] & \cdots & [m_N] \end{bmatrix}$$

nella diagonale principale si trovano le matrici di massa $(3 \times 3)$ di ciascun corpo, mentre altrove avremo tutti minori $3 \times 3$ identicamente nulli.

Allo stesso modo è possibile incolonnare le variabili lagrangiane di tutti gli N corpi in un unico vettore:

$$\{q\} = \begin{Bmatrix} \{q\}_I \\ \{q\}_{II} \\ \vdots \\ \{q\}_N \end{Bmatrix} \qquad \text{le coordinate ovviamente sono } m = 3N$$

questa operazione può essere fatta, analogamente, per i vettori $\{f\}$ e $\{r\}$; per cui si giunge a questa equazione valida per gli N corpi:

$$\boxed{[M]_{m \times m} \{\ddot{q}\}_m = \{f\}_m + \{r\}_m}$$

**EQUAZIONI DELLA DINAMICA** — insieme delle equazioni cardinali della dinamica nel piano per N corpi.

Se i corpi del sistema fossero indipendenti uno dall'altro, avremmo potuto studiare la dinamica in maniera completamente separata; tuttavia nei nostri problemi sono presenti vincoli quindi tra i corpi e quindi non è possibile studiare la dinamica senza risolvere prima la cinematica:

$$\begin{cases} [M]\{\ddot{q}\} = \{f\} + \{r\} & \quad \text{equazione della dinamica} \\ \{\Psi(q)\} = 0 & \quad \text{equazioni di vincolo} \end{cases}$$

Per legarle all'equazione della dinamica, deriviamo rispetto al tempo le equazioni di vincolo:
