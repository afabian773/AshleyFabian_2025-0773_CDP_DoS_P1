# AshleyFabian_2025-0773_CDP_DoS_P1

## Ataque DoS mediante el protocolo CDP
**Estudiante:** Ashley Fabian  
**Matrícula:** 2025-0773  
**Práctica:** P1  
**Asignatura:** Seguridad en Redes  
**Plataforma:** GNS3 — Kali Linux  

---

## Descripción

Este repositorio contiene el script y la documentación técnica del ataque de Denegación de Servicio (DoS) mediante el protocolo CDP (Cisco Discovery Protocol). El atacante genera paquetes CDP con Device-IDs y MACs aleatorias a alta velocidad, agotando la tabla CDP del switch objetivo y elevando su CPU.

---

## Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `AshleyFabian_2025-0773_CDP_DoS_P1.py` | Script del ataque |
| `AshleyFabian_2025-0773_Informe_CDP_DoS_P1.pdf` | Documentación técnica profesional |

---

## Topología de red

| Dispositivo | IP | Puerto |
|---|---|---|
| R1 (CSR1000v) | 25.7.73.1/24 | Gi1 → SW1 Gi0/0 |
| SW1 (vIOS L2) | 25.7.73.2/24 | Gi0/1→VPCS, Gi0/2→Kali |
| Kali Linux | 25.7.73.50/24 | eth0 → SW1 Gi0/2 |
| VPCS (PC1) | 25.7.73.20/24 | eth0 → SW1 Gi0/1 |

**Red:** 25.7.73.0/24 (basada en matrícula 2025-0773)

---

## Uso del script

```bash
# Instalar dependencia
sudo apt install python3-scapy

# Ejecutar el ataque
sudo python3 AshleyFabian_2025-0773_CDP_DoS_P1.py -i eth0 -c 1000

# Parámetros disponibles
# -i  Interfaz de red (ej: eth0)
# -c  Cantidad de paquetes (0=infinito)
# -d  Delay entre paquetes en segundos
```

---

## Contra-medida

```
SW1(config)# interface GigabitEthernet0/2
SW1(config-if)# no cdp enable
```

---

## Video de demostración

🎬 [Ver video en YouTube](https://youtu.be/nr_MJ25-szo?si=vsF4rkbf7Y854Pw3)

> El video muestra el ataque en funcionamiento y la aplicación de la contra-medida.

---

## Requisitos

- Kali Linux
- Python 3.6+
- Scapy: `sudo apt install python3-scapy`
- GNS3 con CSR1000v y vIOS L2
- Ejecutar como root
