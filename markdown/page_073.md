# Page 73 - Analisi del problema (Energia persa nel rotolamento)

## Analisi del problema

L'energia persa in un singolo urto, sarà data dalla differenza fra l'energia di deformazione $E_d$ e quella che viene restituita elasticamente "$\varepsilon E_d$"

$$E_{P_1} = (1 - \varepsilon) E_d$$

dove $\varepsilon$ è il **GRADO DI ELASTICITÀ**, che sarà $\varepsilon = 1$ per materiali perfettamente elastici e $\varepsilon = 0$ per materiali plastici; quindi si definisce $(1 - \varepsilon)$ il **DIFETTO DI ELASTICITÀ**, che sarà "0" per i materiali elastici e "1" per quelli plastici.

Per la conservazione dell'energia, $E_d = E_c$ = energia cinetica posseduta dal punto del disco, per cui

$$E_{P_1} = (1 - \varepsilon) E_c$$

dove $E_c = \frac{1}{2} \frac{Q}{g} V_B^2 = \frac{1}{2} \frac{Q}{g} \omega^2 \rho B^2$ da cui:

$$\boxed{E_{P_1} = (1 - \varepsilon) \frac{Q}{2g} \omega^2 \rho B^2}$$

Inoltre i triangoli $\widehat{AHB}$ e $\widehat{ABC}$ sono simili, per cui vale la proporzione:

$$\frac{AB}{AC} = \frac{AH}{AB}$$

dove $AH = \lambda_n$ ; $AC = 2R$ ; $AB = \rho B$

da cui si ricava $\rho B^2 = 2R\lambda_n$

e sostituendo nella relazione precedente:

$$E_{P_1} = (1 - \varepsilon) \frac{Q}{2g} \cdot 2R\lambda_n \omega^2 =$$

moltiplico e divido per $R$:

$$= (1 - \varepsilon) \cdot \frac{Q}{g} \cdot \frac{(\omega \cdot R)^2}{R} \cdot \lambda_n = (1 - \varepsilon) \cdot \frac{Q}{g} \cdot \frac{V^2}{R} \cdot \lambda_n$$

dove $V = \omega R = \omega \cdot \rho_0 O$ è la velocità che possiede il centro del disco rotolante (avanzamento del disco).

$$\boxed{E_{P_1} = (1 - \varepsilon) \frac{Q}{g} \cdot \frac{V^2}{R} \cdot \lambda_n}$$
**ENERGIA PERSA IN UN SINGOLO URTO**

---

Anche in questo caso si può riconoscere un coefficiente di attrito confrontandoci con la situazione di strisciamento della massa su un piano (attrito radente):

$$①\quad L_P = T \cdot s = (Q \cdot f) \cdot 1 = Q \cdot f \quad \text{(spazio percorso unitario)}$$

lavoro speso su un tratto unitario.

Nel caso del rotolamento, invece, si possono avere un certo numero di urti nello spazio unitario, a seconda di quanto vale $\ell$:

$$n^°_{urti} = \frac{s}{\ell} = \frac{1}{\ell}$$
