# Page 132 - Partizionamento delle coordinate e eliminazione dei vincoli

Come prima, riscriviamo l'equazione sfruttando il partizionamento delle coordinate

$$
\begin{bmatrix} [M^{uu}] & [M^{u\sigma}] \\ {}_{P \times P} & {}_{P \times F} \\ [M^{\sigma u}] & [M^{\sigma\sigma}] \\ {}_{F \times P} & {}_{F \times F} \end{bmatrix} \begin{Bmatrix} \{\ddot{u}\} \\ {}_{P} \\ \{\ddot{\sigma}\} \\ {}_{F} \end{Bmatrix} + \begin{bmatrix} [\Psi_u]^T \\ {}_{P \times P} \\ [\Psi_\sigma]^T \\ {}_{F \times P} \end{bmatrix} \{\lambda\}_{P} = \begin{Bmatrix} \{f_u\} \\ \{f_\sigma\} \\ {}_{F} \end{Bmatrix} \quad ①
$$

Allo stesso modo possiamo riscrivere i vincoli sulle accelerazioni

$$
\{\hat{\delta}\}_{P} = [[\Psi_u][\Psi_\sigma]] \cdot \begin{Bmatrix} \{\ddot{u}\} \\ {}_{P} \\ \{\ddot{\sigma}\} \\ {}_{F} \end{Bmatrix} \underbrace{\text{prodotto riga-colonna}}_{}  \quad \Longrightarrow \quad [\Psi_u]\{\ddot{u}\}_{P \times P} + [\Psi_\sigma]\{\ddot{\sigma}\}_{P \times F} = \{\hat{\delta}\} \quad ②
$$

Dalla ① e dalla ② ho ricavato 3 equazioni vettoriali:

$$
[M^{uu}]_{P \times P}\{\ddot{u}\}_{P} + [M^{u\sigma}]_{P \times F}\{\ddot{\sigma}\}_{F} + [\Psi_u]^T_{P \times P}\{\lambda\}_{P} = \{f_u\}_{P} \qquad \text{"P" equazioni}
$$

$$
\boxed{[M^{\sigma u}]_{F \times P}\{\ddot{u}\}_{P} + [M^{\sigma\sigma}]_{F \times F}\{\ddot{\sigma}\}_{F} + [\Psi_\sigma]^T_{F \times P}\{\lambda\}_{P} = \{f_\sigma\}_{F}} \quad ⑤ \qquad \text{"F" equazioni}
$$

$$
[\Psi_u]_{P \times P}\{\ddot{u}\}_{P} + [\Psi_\sigma]_{P \times F}\{\ddot{\sigma}\}_{F} = \{\hat{\delta}\}_{P} \qquad \text{"P" equazioni}
$$

Adesso in totale abbiamo $P + F + P = M + P$ equazioni; grazie alle quali è possibile ricavare le $\{\ddot{\sigma}\}$ con cui conosco l'evoluzione di tutto il sistema! Quindi adesso devo "eliminare" le $\{\ddot{u}\}$ e i $\{\lambda\}$, così che rimangano le $\{\ddot{\sigma}\}$ come uniche incognite.

Ricavo le $\{\ddot{u}\}$ dall'ultima equazione:

$$
\boxed{\{\ddot{u}\} = [\Psi_u]^{-1}\{\hat{\delta}\} - [\Psi_u]^{-1}[\Psi_\sigma]\{\ddot{\sigma}\}} \quad ③
$$

sostituisco questa nella 1ª equazione, e da essa ricavo le $\{\lambda\}$:

$$
[M^{uu}][\Psi_u]^{-1}\{\hat{\delta}\} - [M^{uu}]\underbrace{[\Psi_u^{-1}][\Psi_\sigma]}_{[M^{uu}] \cdot \{\ddot{u}\}}\{\ddot{\sigma}\} + [M^{u\sigma}]\{\ddot{\sigma}\} + [\Psi_u]^T\{\lambda\} = \{f_u\}
$$

$$
\boxed{\{\lambda\} = ([\Psi_u]^{-1})^T (\{f_u\} + \{[M^{uu}] + [M^{u\sigma}][\Psi_u]^{-1}[\Psi_\sigma]\}\{\ddot{\sigma}\} - [M^{uu}][\Psi_u]^{-1}\{\hat{\delta}\})} \quad ④
$$

Adesso sostituisco ③ e ④ nella ⑤

$$
[M^{\sigma u}][\Psi_u]^{-1}\{\hat{\delta}\} - [M^{\sigma u}][\Psi_u]^{-1}[\Psi_\sigma]\{\ddot{\sigma}\} + [M^{\sigma\sigma}]\{\ddot{\sigma}\} + [\Psi_\sigma]^T[\Psi_u]^{-T}\{f_u\} +
$$

$$
+ [\Psi_\sigma]^T([\Psi_u]^{-1})^T\{[M^{uu}][\Psi_u]^{-1}[\Psi_\sigma] - [M^{u\sigma}]\}\{\ddot{\sigma}\} - [\Psi_\sigma]^T([\Psi_u]^{-1})^T[M^{uu}][\Psi_u]^{-1}\{\hat{\delta}\} = \{f_\sigma\}
$$

questa equazione può essere ricondotta ad una di questo tipo:
