# Page 8 - Soluzione Configurazione Iniziale (Newton-Raphson)

## SOLUZIONE CONFIGURAZIONE INIZIALE (NEWTON-RAPHSON)

Supponiamo di avere una funzione $\Psi(u)$ con questo andamento:

> ![Grafico della funzione Ψ(u) con andamento curvilineo che mostra il metodo di Newton-Raphson. Si vede la curva con i punti $u^{(0)}$, $u^{(1)}$, $u^{(2)}$ sull'asse u, i valori $\Psi[u^{(0)}]$ e $\Psi[u^{(1)}]$ sulla curva, e l'angolo $\beta$ formato dalla tangente alla curva nel punto $u^{(0)}$.](../pages/page_008.png)

Dal grafico si può scrivere che $[u^{(0)} - u^{(1)}] \cdot \text{tg} \, \beta = \Psi[u^{(0)}]$

ma $\text{tg} \, \beta$ è la derivata della funzione calcolata in $u^{(0)}$: $\text{tg} \, \beta = \frac{\partial \Psi(u)}{\partial u}\bigg|_{u^{(0)}}$

da cui ricavo: $[u^{(0)} - u^{(1)}] \cdot \frac{\partial \Psi(u)}{\partial u}\bigg|_{u^{(0)}} = \Psi[u^{(0)}] \longrightarrow u^{(1)} = u^{(0)} - \left[\frac{\partial \Psi(u)}{\partial u}\bigg|_{u^{(0)}}\right]^{-1} \Psi[u^{(0)}]$

quindi generalizzando all'i-esima iterazione:

$$\boxed{u^{(i+1)} = u^{(i)} - \left[\frac{\partial \Psi(u)}{\partial u}\bigg|_{u^{(i)}}\right]^{-1} \cdot \Psi[u^{(i)}]}$$

Passando al caso generale $\{\Psi(u)\}$ = vettore funzione delle variabili $\{u\}$, si consideri lo sviluppo in serie di Taylor:

$$\{\Psi(u + \delta u)\} = \{\Psi(u)\} + [\Psi_u |_{(u^{(i)})}] \cdot \{\delta u\}$$

$\{\delta u\}$ sarà tale da annullare $\{\Psi(u + \delta u)\} = \{0\}$; inoltre avremo un $\mathfrak{Q}\{\delta u\}$ tale che $\{\delta u\} = \{u^{(i+1)}\} - \{u^{(i)}\}$, per cui otteniamo la forma iterativa:

$$0 = [\Psi_u |_{(u^{(i)})}]^{-1} \{\Psi(u)\} + \{u^{(i+1)}\} - \{u^{(i)}\} \longrightarrow \boxed{\{u^{(i+1)}\} = \{u^{(i)}\} - [\Psi_u |_{(u^{(i)})}]^{-1} \{\Psi(u)\}}$$

$[\Psi_u |_{(u^{(i)})}]$ = matrice Jacobiana del vettore delle funzioni di vincolo $\{\Psi(u)\}$
