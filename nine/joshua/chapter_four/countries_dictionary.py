# Author: Joshua
# Title : This gives various Information about different Countries

nation_details = {"asia": [
    {"country": "Afghanistan", "Capital": "Kabul", "currency": "Afghani", "language": ["Dari Persian", "Pashto"]},
    {"country": "Azerbaijan", "capital": "Baku", "currency": "Manat", "language": ["Azerbaijani"]},
    {"country": "Bahrain", "capital": "Manama", "currency": "Bahraini Dinar", "language": ["Arabic"]},
    {"country": "Bangladesh", "capital": "Dhaka", "currency": "Taka", "language": ["Bangla"]},
    {"country": "Cambodia", "capital": "Phnom Penh", "currency": "Riel", "language": ["Khmer"]}
    ],
                  "europe": [{"country": "Albania", "capital": "Tirane", "currency": "Lek", "language": ["Albanian"]},
                             {"country": "Andorra", "capital": "Andorra la Vella", "currency": "Euro",
                              "language": ["Catalan"]},
                             {"country": "Armenia", "capital": "Yerevan", "currency": "Dram", "language": ["Armenian"]},
                             {"country": "Austria", "capital": "Vienna", "currency": "Euro", "language": ["German"]},
                             {"country": "Belgium", "capital": "Brussels", "currency": "Euro",
                              "language": ["Dutch", "French", "German"]},
                             {"country": "Bosnia and Herzegovina", "capital": "Sarajevo",
                              "currency": "Convertible Mark", "language": ["Bosnian", "Croatian", "Serbian"]},
                             {"country": "Bulgaria", "capital": "Sofia", "currency": "Lev", "language": ["Bulgarian"]}
                             ],
                  "africa": [{"country": "Algeria", "capital": "Algiers", "currency": "Algerian Dinar",
                              "language": ["Arabic", "Tamazight", "French"]},
                             {"country": "Angola", "capital": "Luanda", "currency": "Kwanza",
                              "language": ["Portuguese"]},
                             {"country": "Benin", "capital": "Porto-Novo", "currency": "West African CFA Franc",
                              "language": ["Kirundi", "French"]},
                             {"country": "Botswana", "capital": "Gaborone", "currency": "Pula",
                              "language": ["Tswana", "English"]},
                             {"country": "Burkina Faso", "capital": "Ouagadougou", "currency": "West African CFA Franc",
                              "language": ["French"]},
                             {"country": "Burundi", "capital": "Bujumbura", "currency": "Burundi Franc",
                              "language": ["French"]},
                             {"country": "Cameroon", "capital": "Yaounde", "currency": "Central African CFA Franc",
                              "language": ["French", "English"]},
                             {"country": "Cape Verde", "capital": "Praia", "currency": "Cape Verdean Escudo",
                              "language": ["Portuguese"]},
                             {"country": "Central African Republic", "capital": "Bangui",
                              "currency": "Central African CFA Franc", "language": ["Sango", "French"]}

                             ],
                  "south America": [{"country": "Argentina", "capital": "Buenos Aires", "currency": "Argentine Peso",
                                     "language": ["Spanish"]},
                                    {"country": "Bolivia", "capital": "La Paz", "currency": "Boliviano",
                                     "language": ["Spanish", "Quechua", "Aymara"]},
                                    {"country": "Brazil", "capital": "Brasilia", "currency": "Real",
                                     "language": ["Portuguese"]}
                                    ],
                  "australia": [{"country": "Australia", "capital": "Canberra", "currency": "Australian Dollar",
                                 "language": ["English"]}],
                  "North America": [{"country": "Bahamas", "capital": "Nassau", "currency": "Bahamian Dollar",
                                     "language": ["English"]},
                                    {"country": "Barbados", "capital": "Bridgetown", "currency": "Barbadian Dollar",
                                     "language": ["English"]},
                                    {"country": "Canada", "capital": "Ottawa", "currency": "Canadian Dollar",
                                     "language": ["English", "French"]}
                                    ]
                  }
for i in range(len("asia")):
    print(nation_details["asia"][i]["language"][0])

