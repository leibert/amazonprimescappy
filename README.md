# Amazon-Dash-Scapy
Script that sits on a Raspberry pi looking for Amazon Dash buttons that might be pushed. If it sees one, it'll tell an ESP to do something.

Implemented in the coffee signal light. When coffee has been brewed you press the nearby Amazon dash button, scapy detects in, then tells an ESPNode to start blinking the HMI light stack
<p align="center">
<img src="http://images.cwm.eml.cc/coffee2.jpg?variant=small" width = "20%" height="20%">
<img src="http://images.cwm.eml.cc/coffee1.jpg?variant=small" width = "20%" height="20%">
</p>
After 45 minutes, the red light starts blinking to denote the lesser freshness. Finally after an 90 minutes or so, the light stack stops blinking.
