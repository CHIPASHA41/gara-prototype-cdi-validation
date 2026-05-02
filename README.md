# GARA Prototype CDI Validation

This repository contains a Mininet-based prototype for validating the Architectural Enforcement Layer of the Governance–Architecture Risk Alignment (GARA) framework.

## Objective

To demonstrate that governance-derived cybersecurity directives can be translated into enforceable architectural controls in a Critical Digital Infrastructure (CDI) environment.

## Topology

The emulation consists of four zones:

- Corporate IT Zone
- DMZ / Mediation Zone
- OT Zone
- SOC / Monitoring Zone

## Key Results

| Test | Baseline | GARA-Enforced |
|---|---|---|
| IT to OT connectivity | Allowed | Blocked |
| IT reconnaissance | Host reachable | Filtered |
| DMZ to OT | Allowed | Allowed |
| OT to SOC | Allowed | Allowed |
| Enforcement evidence | None | 4003 packets dropped |

## GARA Indicators

- PCCR = 1.00
- EVR = 1.00
- ARI = 1.00 (within experimental scope)

## Structure

- `topology/` → Mininet topology
- `experiments/` → Results
- `figures/` → Diagrams
- `paper/` → Manuscript sections
- `scripts/` → Future automation

## Tools

- Kali Linux (WSL)
- Mininet
- Open vSwitch
- Nmap

## Author

Cornelius Chipasha
