# Page 86 - Gradiente di pressione e spinta risultante (cuscinetto a pattino)

Essendoci un diagramma delle pressioni, esisterà anche una spinta risultante verso l'alto, che può bilanciare un carico eventuale (a differenza del moto con $h = \text{cost}$).

Questa spinta si è generata solo grazie alla dinamica del problema, ma per calcolare la occorre conoscere il diagramma delle pressioni: sfruttiamo la costanza della portata.

Tolta $Q$ si ha: $\underset{\text{PORTATA IN } \bar{x}}{Q(\bar{x})} = \frac{V\bar{h}}{2}$ e $Q(x) = \frac{Vh}{2} - \frac{P'h^3}{12\mu}$ ← PORTATA IN UN PUNTO GENERICO

che devono essere uguali, per cui:

$$\frac{V\bar{h}}{2} = \frac{Vh}{2} - \frac{P'h^3}{12\mu} \quad \Rightarrow \quad \frac{P'h^3}{6\mu} = V(h - \bar{h})$$

$$\boxed{P' = \frac{6\mu \, V(h - \bar{h})}{h^3}} \qquad \text{GRADIENTE DI PRESSIONE}$$

Da questa basterà integrare tra "0" e un generico "x" per ottenere:

$$\boxed{P(x) = \int_0^x \frac{6\mu \, V(h - \bar{h})}{h^3} \, dx} \qquad \text{DIAGRAMMA DELLE PRESSIONI}$$

Infine si può integrare anche il diagramma delle pressioni per ottenere la:

$$\boxed{N = \int_0^x P(x) \, dx} \qquad \text{SPINTA RISULTANTE}$$

che sarà una forza per unità di lunghezza, in quanto la $Y$ è unitaria!

Si può calcolare anche la retta d'azione della risultante $\bar{N}$, trovando che essa sia **EQUIVALENTE** al sistema di forze infinitesime agenti su ogni $dx$; e ciò avviene assumendo che $\bar{N}$ (applicata lungo la propria retta d'azione) abbia un momento nullo, calcolato rispetto alla sezione di entrata, uguale alla somma dei momenti statici del sistema di forze elementari di pressione:

$$\boxed{X_N \cdot N = \int_0^l x \cdot P(x) \, dx} \qquad \text{RETTA D'AZIONE}$$

È possibile ricavare anche l'azione tangenziale necessaria a muovere la slitta superficiale, integrando lungo il tratto la "$\tau$" della formula del Petroff, calcolata in $z = h$:

$$\boxed{T = \int_0^l \mu \left. \frac{\partial u}{\partial z} \right|_{z=h} dx} \qquad \text{AZIONE TANGENZIALE}$$

In questo modo è possibile introdurre un **COEFFICIENTE DI ATTRITO MEDIATO**
