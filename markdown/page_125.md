# Page 125 - Analisi Cinematica dei Meccanismi: Semplificazioni e Equazioni di Vincolo sulle Velocità

Per l'analisi cinematica dei meccanismi si riscrivono queste due equazioni tenendo conto di due **SEMPLIFICAZIONI**:

1. I vincoli non dipendono dal tempo, per cui tutti i termini $\frac{\partial}{\partial t}$ delle equazioni di vincolo verranno annullati! Sia per velocità sia per accelerazioni.

2. Partizioniamo le coordinate lagrangiane:

$$\{q\} = \begin{Bmatrix} \dot{u} \\ \dot{\sigma} \end{Bmatrix} \quad M = P + F$$

così da poter scrivere le equazioni di vincolo come $\{\Psi(u, \hat{\sigma})\} = \{\phi\}$ dove le $\hat{\sigma}$ sono le variabili che vengono fissate e con le quali si calcolano le "$u$" da esse dipendenti.

Riferendoci al risultato ottenuto per le velocità, operazione che sfruttando solo la prima semplificazione, la I$^a$ equazione di vincolo diventa:

$$\boxed{[\Psi_q] \cdot \{\dot{q}\} = \{\phi\}}$$
$$\underset{P \times M}{} \quad \underset{M}{} \quad \underset{P}{}$$

Adesso rifacciamo i calcoli includendo anche il partizionamento: ordiniamo le coordinate in modo che compaiano prima le "$u$" e poi le "$\sigma$"

$$\underset{P \times M}{[\Psi_q]} = \left[ \underset{P \times P}{[\Psi_u]} \mid \underset{P \times F}{[\Psi_\sigma]} \right] \cdot \begin{Bmatrix} \{\dot{u}\} \\ \{\dot{\sigma}\} \end{Bmatrix} = \{\phi\}$$

$$\longrightarrow \{q\}_M$$

da cui ottengo:

$$\boxed{\underset{P \times P}{[\Psi_u]} \{\dot{u}\} + \underset{P \times F}{[\Psi_\sigma]} \{\dot{\sigma}\} = \{\phi\}} \quad \textcircled{R}$$

moltiplico a sinistra per l'inversa di $[\Psi_u]$, così da esplicitare $\{\dot{u}\}$

$$\{\dot{u}\} = -\underset{P \times P}{[\Psi_u]^{-1}} \underset{P \times F}{[\Psi_\sigma]} \{\dot{\sigma}\} \quad \text{dove} \quad \boxed{[R] = -[\Psi_u]^{-1} [\Psi_\sigma]} \quad \frac{\text{MATRICE DEI RAP-}}{\text{PORTI DELLE VELOCITÀ}}$$

quindi si ottiene:

$$\boxed{\{\dot{u}\}_P = [R]_{P \times F} \{\dot{\sigma}\}_F} \quad \text{I}^a \text{ EQUAZIONE DI VINCOLO SULLE VELOCITÀ (SEMPLIFICATA)}$$

avendo dovuto invertire $[\Psi_u]$ si suppone che per le configurazioni critiche, in cui $\det = 0$, non si possa effettuare nemmeno l'analisi al primo ordine: $\det[\Psi_u] \neq 0$ è una condizione obbligatoria per conoscere tutte le velocità in maniera univoca.

Ovviamente anche nello studio al primo e al secondo ordine, dovrò assegnare velocità e accelerazioni delle variabili indipendenti $\{\dot{\sigma}\}$.
