# Page 195 - Trasmissione omocinetica (giunti per alberi sghembi)

individua $C_2$, grazie all'intersezione tra $\overline{C_1 K}$ e l'ortogonale ad $a_1$ in $D_1$!

Siccome $C_1, C_2$ e $K$ sono allineati, vale sicuramente che:

$$C_1 K = C_1 C_2 + C_2 K \quad (1)$$

quindi se chiamiamo $D_1 C_2 = h_1$ e $D_2 C_1 = h_2$, posso sfruttare i triangoli rettangoli $D_1 \hat{C}_2 K$ e $D_2 \hat{C}_1 K$ per scrivere che:

$$\begin{cases} C_2 K = h_1 \tan \vartheta_1 \\ C_1 K = h_2 \tan \vartheta_2 \end{cases}$$

ed inoltre avremo $C_1 C_2 = A_1 A_2 = d$

per cui sostituendo in $(1)$:

$$h_2 \tan \vartheta_2 = d + h_1 \tan \vartheta_1 \longrightarrow \boxed{\tan \vartheta_2 = \frac{d}{h_2} + \frac{h_1}{h_2} \tan \vartheta_1} \quad (*)$$

Derivo l'ultima espressione rispetto al tempo:

$$\frac{d}{dt}(\tan \vartheta) = \frac{d}{dt}\left(\frac{\sin \vartheta}{\cos \vartheta}\right) = \frac{\cos^2 \vartheta + \sin^2 \vartheta}{\cos^2 \vartheta} = 1 + \tan^2 \vartheta \quad \text{oppure} \quad \frac{1}{\cos^2 \vartheta}$$

$$\ddot{\vartheta}_2 (1 + \tan^2 \vartheta_2) = \frac{h_1}{h_2} \cdot \dot{\vartheta}_1 (1 + \tan^2 \vartheta_1)$$

quindi mi scrivo il rapporto di trasmissione, che dovrà porsi a "1" per avere la condizione di omocineticità:

$$\tau = \frac{\omega_2}{\omega_1} = \frac{h_1 (1 + \tan^2 \vartheta_1)}{h_2 (1 + \tan^2 \vartheta_2)} \xrightarrow{(*)} \boxed{\frac{h_1 (1 + \tan^2 \vartheta_1)}{h_2 \left[1 + \left(\frac{d}{h_2} + \frac{h_1}{h_2} \tan \vartheta_1\right)^2\right]} = \tau}$$

Affinché sia verificata la condizione di omocineticità ($\tau = 1$), deve valere sia che $h_1 = h_2$ e sia che $d = 0$ $\Rightarrow$ gli assi "$a_1$" e "$a_2$" non possono essere sghembi, per cui "**non è ottenibile una trasmissione omocinetica per alberi appartenenti a piani diversi**".
