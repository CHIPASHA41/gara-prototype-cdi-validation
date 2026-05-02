## IV-H. Prototype Validation Using Mininet Emulation

A Mininet-based prototype was developed to validate the enforceability of the GARA Architectural Enforcement Layer. The objective was to demonstrate that governance-derived directives can be translated into enforceable network controls and verified using measurable evidence.

The emulated environment consisted of four logical zones: Corporate IT, DMZ/Mediation, OT, and SOC/Monitoring. In the baseline configuration, all nodes were fully reachable. The `pingall` test reported 0% packet loss, and Nmap scans confirmed that OT hosts were directly reachable from Corporate IT systems. This demonstrates the policy–enforcement gap.

Following GARA enforcement, a default-deny OpenFlow rule was applied to block direct IT-to-OT communication. Post-enforcement testing showed that ICMP connectivity from Corporate IT host `h1` to OT hosts failed with 100% packet loss. Nmap scans transitioned from “closed” to “filtered,” indicating that reconnaissance traffic was blocked.

Legitimate communication paths were preserved. DMZ-to-OT communication (`h3 → h4`) remained successful, and OT-to-SOC communication (`h4 → h6`) was unaffected.

Flow-level verification confirmed enforcement effectiveness. Over 4000 packets were matched and dropped by the OpenFlow rule, demonstrating active, measurable enforcement.

These results confirm that GARA enables translation of governance directives into enforceable architectural controls.
