# Page 120 - Momento d'inerzia equivalente (manovellismo)

$m_A \cdot a - m_B \cdot b = 0$ ② (conservazione del baricentro)

$m_A \cdot a^2 + m_B \cdot b^2 = I_{G_3}$ ③ (conservazione del momento d'inerzia)

Mettendo a sistema ①, ② e ③ si otterrebbero le singole masse; ma per semplificare ulteriormente la situazione decidiamo di trascurare $m_{G_3}$, ossia di rinunciare anche alla ③, commettendo un errore trascurabile:

$$\begin{cases} m_A + m_B = m_3 \\ m_A \cdot a = m_B \cdot b \end{cases} \longrightarrow m_A + m_A \frac{a}{b} = m_3 \; ;$$

$$m_A \left(\frac{a + b}{b}\right) = m_3 \implies \boxed{m_A = m_3 \frac{b}{l}}$$

quindi: $\quad m_B = \frac{a}{b} \cdot m_3 \frac{b}{l} \longrightarrow \boxed{m_B = m_3 \frac{a}{l}}$

---

Adesso scriviamo la conservazione dell'energia cinetica, tenendo conto dei contributi di $m_A$, $m_B$, $m_4$ e $m_2$: $m_B$ ed $m_4$ sono le masse concentrate sullo stantuffo 4, la cui energia cinetica dipenderà da $v_B$; mentre $m_2$ contribuisce col momento d'inerzia noto $I_2$, ossia "$\frac{1}{2} I_2 \omega^2$"; e $m_A$ contribuisce ruotando attorno all'albero di riduzione $A_o$, ossia "$m_A \cdot r^2$" $\longrightarrow$ "$\frac{1}{2} (m_A r^2 \omega^2)$"

La $v_B$ dello stantuffo emerge dallo studio del cinematismo:

$$v_B^2 = \omega^2 r^2 \left(\frac{1}{2} + \frac{\lambda^2}{8}\right) \quad \text{dove } \lambda = \frac{r}{l} \quad \text{(snellezza)}$$

## Conservazione energia cinetica

$$\boxed{\frac{1}{2} I_e \omega^2 = \frac{1}{2} (I_2 + m_A r^2) \omega^2 + \frac{1}{2} (m_4 + m_B) v_B^2}$$

Sostituisco $v_B$:

$$I_e \omega^2 = (I_2 + m_A r^2) \omega^2 + (m_4 + m_B) \omega^2 r^2 \left(\frac{1}{2} + \frac{\lambda^2}{8}\right)$$

$$\boxed{I_e = I_2 + m_A r^2 + (m_4 + m_B)\left(\frac{1}{2} + \frac{\lambda^2}{8}\right) r^2}$$
