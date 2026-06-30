# Page 83 - Bilancio locale delle forze e profilo di velocità nel meato

Il bilancio locale delle forze sarà:

$$P(x) \cdot d\bar{z} \cdot 1 - [P(x) + P' \cdot dx] \cdot d\bar{z} \cdot 1 + [\tau(\bar{z}) + \frac{d\tau}{d\bar{z}} d\bar{z}] \cdot dx \cdot 1 - \tau(\bar{z}) \cdot dx \cdot 1 = 0$$

$$-P' \cdot dx \cdot d\bar{z} + \frac{d\tau}{d\bar{z}} \cdot dx \cdot d\bar{z} = 0 \quad \longrightarrow \quad P' = \frac{d\tau}{d\bar{z}}$$

Sfruttando la formula del Newton $\tau = \frac{du}{d\bar{z}} \cdot \mu$, quindi sostituendo:

$$P' = \mu \cdot \frac{d^2 u}{d\bar{z}^2} \quad \longrightarrow \quad \boxed{\frac{d^2 u}{d\bar{z}^2} = \frac{P'}{\mu}}$$

Grazie a questa equazione differenziale, sarà possibile risolvere il problema, trovando il diagramma delle pressioni, semplicemente accoppiando le giuste condizioni al contorno.

Queste saranno date dai valori di $u(\bar{z})$ nei due piani esterni, in cui si assume che l'olio abbia la stessa velocità dei piani stessi per fenomeni di adesione:

$$\boxed{u(0) = 0}$$

$$\boxed{u(h) = V}$$

Integrando due volte l'equazione differenziale:

$$\frac{d^2 u}{d\bar{z}^2} = \frac{P'}{\mu} \xrightarrow{\text{integro}} \frac{du}{d\bar{z}} = \frac{P'}{\mu} \bar{z} + A \xrightarrow{\text{integro}} u(\bar{z}) = \frac{1}{2} \frac{P'}{\mu} \bar{z}^2 + A\bar{z} + B$$

**1ª condizione al contorno:**

$$u(0) = B = 0 \quad \longrightarrow \quad \boxed{B = 0}$$

**2ª condizione al contorno:**

$$u(h) = \frac{1}{2} \frac{P'}{\mu} h^2 + Ah = V \quad \longrightarrow \quad \boxed{A = \frac{V}{h} - \frac{1}{2} \frac{P'}{\mu} h}$$

**Sostituendo nell'equazione integrata:**

$$u(\bar{z}) = \frac{1}{2} \frac{P'}{\mu} \bar{z}^2 + \frac{V}{h} \bar{z} - \frac{1}{2} \frac{P'}{\mu} h \cdot \bar{z} \quad \longrightarrow \quad \boxed{u(\bar{z}) = \frac{V}{h} \bar{z} - \frac{1}{2} \frac{P'}{\mu} \bar{z} (h - \bar{z})}$$

> **VELOCITÀ GENERICA FATTA DA FLUIDA IN UN MEATO DI ALTEZZA $h$**

Avremo un contributo lineare $\frac{V}{h} \bar{z}$, che va da "0" a "V"; oltre ad un contributo parabolico, che assume valore nullo agli estremi, per cui potranno essere rappresentati con i seguenti diagrammi, la cui somma fornisce il diagramma totale:
