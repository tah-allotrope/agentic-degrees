# 0001 · MEASUR-before-REopt and why heat_pump_model's costs are radioactive

Weeks 1–2, strongest non-obvious insights: (1) the toolchain has a strict ordering — MEASUR
shrinks the steam load first, REopt sizes replacement heat second — because capital dominates
a heat pump's LCOH, so sizing against an unoptimized load inflates LCOH almost linearly
(~30% over-buy per ee-heat's own note); (2) `heat_pump_model` is trusted for COP (CoolProp
physics, reproduced 6.22→3.11 three independent ways) while its cost output — negative capex,
garbled units, an LCOH below its own energy floor ($2.24 < $6.58/MMBtu) — is wrong by
construction. Audit components of a tool, never the tool's brand.
