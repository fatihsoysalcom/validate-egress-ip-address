# Validate Egress IP Address

This example demonstrates how to programmatically determine the public egress IP address of the machine executing the script. It simulates an application making an outbound connection to an external service and then validates the observed egress IP against a predefined whitelisted IP, as discussed in the accompanying article. This helps verify if network configurations or whitelist updates are working as expected.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [Beyaz Liste Duvarı Yıkıldı mı? Çıkış IP'si Doğrulama Serüveni: 104.28.152.116 Örneği](https://fatihsoysal.com/blog/beyaz-liste-duvari-yikildi-mi-cikis-ipsi-dogrulama-seruveni-104-28-152-116-ornegi/).

## License

MIT — see [LICENSE](LICENSE).
