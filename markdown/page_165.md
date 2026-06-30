# Page 165 - Equazione del moto e Metodo del Rayleigh

to al polo "O", che è il centro della carrucola (equilibrio alla rotazione):

$$-Kx \cdot R - m\ddot{x} \cdot R = I_0 \ddot{\vartheta}$$

dove: $Kx \cdot R$ = richiamo elastico, $m\ddot{x} \cdot R$ = forza di inerzia

Sostituendo la relazione $x = R\vartheta$ nell'equazione:

$$-KR^2 \vartheta - mR^2 \ddot{\vartheta} = \frac{1}{2}MR^2 \ddot{\vartheta}$$

da cui si ottiene l'**EQUAZIONE DEL MOTO**:

$$\boxed{\left(mR^2 + \frac{1}{2}MR^2\right)\ddot{\vartheta} + KR^2 \vartheta = 0}$$

essendo un'equazione del tipo $m\ddot{x} + Kx = 0$ (con $\vartheta$ al posto di $x$), possiamo lavorare per similitudine:

$$\omega_n = \sqrt{\frac{K}{m}} \quad \longrightarrow \quad \omega_n = \sqrt{\frac{KR^2}{mR^2 + \frac{1}{2}MR^2}}$$

da cui si ottiene:

$$\boxed{\omega_n = \sqrt{\frac{2K}{2m + M}}}$$

---

## Metodo del Rayleigh

Partiamo calcolando l'**energia cinetica**:

$$T = \frac{1}{2}m\dot{x}^2 + \frac{1}{2}I_0 \dot{\vartheta}^2$$

(traslazione della massa + rotazione del disco)

Con $x = R\vartheta$:

$$T = \frac{1}{2}mR^2 \dot{\vartheta}^2 + \frac{1}{2} \cdot \frac{1}{2}MR^2 \dot{\vartheta}^2$$

Immaginiamo che il disco segua una legge di oscillazione del tipo:

$$\vartheta = \Theta \cos(\omega t + \varphi) \quad \xrightarrow{\text{derivando}} \quad \dot{\vartheta} = -\omega \Theta \sin(\omega t + \varphi)$$

e siccome dobbiamo fare riferimento al valore massimo di energia cinetica, scriviamo:

$$T_{MAX} = \left(\frac{1}{2}mR^2 + \frac{1}{4}MR^2\right)\omega^2 \Theta^2 \quad \textcircled{1}$$

Adesso calcoliamo l'**energia potenziale**:

$$U = \frac{1}{2}Kx^2 \xrightarrow{x = R\vartheta} U = \frac{1}{2}KR^2 \vartheta^2$$

Riferendoci alla legge di oscillazione precedente si ricava:

$$U_{MAX} = \frac{1}{2}KR^2 \Theta^2 \quad \textcircled{2}$$

Adesso uguagliamo ① e ② per trovare la **pulsazione naturale**:

$$\left(\frac{1}{2}mR^2 + \frac{1}{4}MR^2\right)\omega^2 \Theta^2 = \frac{1}{2}KR^2 \Theta^2$$

$$(2m + M)\omega^2 = 2K \quad \longrightarrow \quad \boxed{\omega_n = \sqrt{\frac{2K}{2m + M}}}$$
