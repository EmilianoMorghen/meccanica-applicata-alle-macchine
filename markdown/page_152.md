# Page 152 - Rotismi Epicicloidali: Velocità Angolari

Da essa ricavo ciascuna delle velocità angolari:

$$\boxed{\begin{cases} \omega_i = \tilde{\tau}_{ij} \, \omega_j + (1 - \tilde{\tau}_{ij}) \, \omega_k \\ \omega_j = \dfrac{1}{\tilde{\tau}_{ij}} \, \omega_i + \dfrac{\tilde{\tau}_{ij} - 1}{\tilde{\tau}_{ij}} \, \omega_k \\ \omega_k = \dfrac{1}{1 - \tilde{\tau}_{ij}} \, \omega_i - \dfrac{\tilde{\tau}_{ij}}{1 - \tilde{\tau}_{ij}} \, \omega_j \end{cases}}$$

Inoltre si può porre nulla, di volta in volta, una di queste $\omega$ e ricavare le varie relazioni:

---

### Se $\boxed{\omega_i = 0}$:

$$0 = \tilde{\tau}_{ij} \, \omega_j + (1 - \tilde{\tau}_{ij}) \, \omega_k$$

| | | |
|---|---|---|
| ruota i | $0$ | $0$ |
| ruota j | $\omega_j$ | $\dfrac{\tilde{\tau}_{ij} - 1}{\tilde{\tau}_{ij}} \, \omega_k$ |
| ruota k | $\dfrac{\tilde{\tau}_{ij}}{\tilde{\tau}_{ij} - 1} \, \omega_j$ | $\omega_k$ |

---

### Se $\boxed{\omega_j = 0}$:

$$\omega_i = (1 - \tilde{\tau}_{ij}) \, \omega_k$$

| | | |
|---|---|---|
| ruota i | $\omega_i$ | $(1 - \tilde{\tau}_{ij}) \, \omega_k$ |
| ruota j | $0$ | $0$ |
| ruota k | $\dfrac{\omega_i}{1 - \tilde{\tau}_{ij}}$ | $\omega_k$ |

---

### Se $\boxed{\omega_k = 0}$:

$$\omega_i = \tilde{\tau}_{ij} \, \omega_j$$

| | | |
|---|---|---|
| ruota i | $\omega_i$ | $\tilde{\tau}_{ij} \, \omega_j$ |
| ruota j | $\dfrac{1}{\tilde{\tau}_{ij}} \, \omega_i$ | $\omega_j$ |
| ruota k | $0$ | $0$ |
