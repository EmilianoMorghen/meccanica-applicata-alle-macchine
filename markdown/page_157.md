# Page 157 - Soluzione con numeri complessi e pulsazione naturale

Per rappresentare la soluzione con i numeri complessi, dovrei utilizzare

$$\boxed{X(t) = \bar{X} \, e^{i\omega t}} \quad \text{①}$$

dove $\bar{X} = A + iB$ e $e^{i\omega t} = \cos\omega t + i \sin\omega t$

per cui $X = (A + iB)(\cos\omega t + i \sin\omega t) \implies \text{Re}(x) = A\cos\omega t - B\sin\omega t$

Derivando la soluzione appena trovata

$$\boxed{\dot{X} = i\omega \, \bar{X} \, e^{i\omega t}}$$

derivando una seconda volta ho

$$\boxed{\ddot{X} = -\omega^2 \, \bar{X} \, e^{i\omega t}} \quad \text{②}$$

Adesso sostituisco ① e ② nell'equazione differenziale:

$$m(-\omega^2 \bar{X} \, e^{i\omega t}) + K \bar{X} \, e^{i\omega t} = 0$$

$$\underbrace{\bar{X} \, e^{i\omega t}}_{} (K - m\omega^2) = 0$$

affinché quest'ultima sia verificata $\forall t$, avremo come possibili soluzioni:

1) $\bar{X} = 0$ — soluzione banale

2) $K - m\omega^2 = 0 \implies \boxed{\omega = \sqrt{\dfrac{K}{m}} = \omega_n}$ — **PULSAZIONE NATURALE** (grandezza fondamentale delle vibrazioni)

e quindi nella soluzione $X(t)$, qualunque sia la forma in cui essa viene scritta, bisognerà avere $\omega = \omega_n$!

Le soluzioni possibili sono:

- 1° tipo: $X(t) = C \cos(\omega_n t + \varphi)$
- 2° tipo: $X(t) = A\cos\omega_n t \mp B\sin\omega_n t$

Per ricavare le costanti $C, \varphi$ oppure $A, B$ bisogna usare le condizioni iniziali:

Per una soluzione del 2° tipo (perché $X(t)$ corrisponde a $\text{Re}(x)$):

$$\begin{cases} X(t) = A\cos\omega_n t - B\sin\omega_n t \\ X(t=0) = x_0 \\ \dot{X}(t=0) = v_0 \end{cases}$$

---

$$X(t=0) = A \implies \boxed{A = x_0}$$

$$\dot{X}(t) = -A\omega_n \sin\omega_n t - B\omega_n \cos\omega_n t \implies \dot{X}(t=0) = -B\omega_n$$

pertanto $-B\omega_n = v_0 \implies \boxed{B = -\dfrac{v_0}{\omega_n}}$

Sostituendo le costanti nella soluzione, essa diventerà

$$\boxed{X(t) = x_0 \cos\omega_n t + \frac{v_0}{\omega_n} \sin\omega_n t}$$
