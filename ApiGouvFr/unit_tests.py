import unittest
import requests
import json


# https://geo.api.gouv.fr/decoupage-administratif
class UnitTestsGeoApiGouvFrDecoupageAdministrative(unittest.TestCase):
    def test_communes(self):
        print("test_communes")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population,centre&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_afficher_code_insee_communes(self):
        print("test_afficher_code_insee_communes")

        url = "https://geo.api.gouv.fr/communes?fields=code,codesPostaux&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_recuperer_les_informations_concernant_une_commune(self):
        print("test_recuperer_les_informations_concernant_une_commune")

        url = "https://geo.api.gouv.fr/communes/95127?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        commune = ''

        commune += json.loads(response.text)
        print(commune)

        code_insee_departement = commune['codeDepartement']
        print("code_insee_departement : " + str(code_insee_departement))

        code_insee_commune = commune['code']
        print("code_insee_commune : " + str(code_insee_commune))

        population = commune['population']
        print("population : " + str(population))

    def test_rechercher_une_commune_avec_son_code_postal(self):
        print("test_rechercher_une_commune_avec_son_code_postal")

        url = "https://geo.api.gouv.fr/communes?codePostal=93260"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_afficher_le_code_insee_d_une_commune_avec_son_code_postal_depuis_contact_excel(self):
        print("test_rechercher_une_commune_avec_son_code_postal")

        contact_excel = "Localisation20 r Villegranges, 93260 LES LILAS".split(",")[1].replace(' ', '')[:5]

        print("contact_excel : " + contact_excel)

        url = "https://geo.api.gouv.fr/communes?codePostal=" + contact_excel

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        code_insee_commune = json.loads(response.text)[0]['code']

        print("code_insee_commune : " + str(code_insee_commune))

    def test_afficher_le_code_insee_d_une_commune_avec_son_code_postal(self):
        print("test_afficher_le_code_insee_d_une_commune_avec_son_code_postal")

        url = "https://geo.api.gouv.fr/communes?codePostal=95800 "

        payload = {}
        headers = {}

        response = requests.request("GET", url.replace(" ", ""), headers=headers, data=payload)

        code_insee_commune = json.loads(response.text)[0]['code']

        print(code_insee_commune)

    def test_afficher_la_population_d_une_commune_avec_son_code_postal(self):
        print("test_afficher_la_population_d_une_commune_avec_son_code_postal")

        url = "https://geo.api.gouv.fr/communes?codePostal=78810 "

        payload = {}
        headers = {}

        response = requests.request("GET", url.replace(" ", ""), headers=headers, data=payload)

        population = json.loads(response.text)[0]['population']

        print(population)

    def test_afficher_le_code_region_d_une_commune_avec_son_code_postal(self):
        print("test_afficher_la_region_d_une_commune_avec_son_code_postal")

        url = "https://geo.api.gouv.fr/communes?codePostal=78810 "

        payload = {}
        headers = {}

        response = requests.request("GET", url.replace(" ", ""), headers=headers, data=payload)

        codeRegion = json.loads(response.text)[0]['codeRegion']

        print(codeRegion)

    def test_rechercher_une_commune_avec_son_code_postal_et_son_nom(self):
        print("test_rechercher_une_commune_avec_son_code_postal")

        nom = "Cergy"

        url = "https://geo.api.gouv.fr/communes?codePostal=95800"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        informations_pour_une_commune_avec_son_code_postal = response.json()

        for commune in informations_pour_une_commune_avec_son_code_postal:
            if commune['nom'] == nom:
                print(commune)

    def test_renvoi_les_communes_pour_un_departement(self):
        print("test_renvoi_les_communes_pour_un_departement")

        url = "https://geo.api.gouv.fr/departements/77/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.json())

        # print(json.loads(response.text))

    def test_renvoi_les_communes_pour_une_region(self):
        print("test_renvoi_les_communes_pour_une_region")

        url = "https://geo.api.gouv.fr/regions/11/communes?fields=code,nom,codesPostaux,codeDepartement,codeRegion,population&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_rechercher_des_departements(self):
        print("test_rechercher_des_departements")

        url = "https://geo.api.gouv.fr/departements?fields=code,nom,codeRegion,region&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_recuperer_les_informations_concernant_un_departement(self):
        print("test_recuperer_les_informations_concernant_un_departement")

        url = "https://geo.api.gouv.fr/departements/75?fields=code,nom,codeRegion,region&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_renvoi_les_departements_dans_une_region(self):
        print("test_renvoi_les_departements_dans_une_region")

        url = "https://geo.api.gouv.fr/regions/11/departements?fields=code,nom,codeRegion,region&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_rechercher_des_regions(self):
        print("test_rechercher_des_regions")

        url = "https://geo.api.gouv.fr/regions?fields=code,nom,codeDepartement&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_afficher_les_regions_pour_annuaire_service_public(self):
        print("test_rechercher_des_regions")

        url = "https://geo.api.gouv.fr/regions?fields=code,nom,codeDepartement&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        regions = json.loads(response.text)

        for region in regions:
            nom_region = region['nom'].lower()\
                .replace('î', 'i')\
                .replace('é', 'e')\
                .replace('è', 'e')\
                .replace('à', 'a')\
                .replace('ô', 'o')\
                .replace("'", '-')\
                .replace(' ', '-')
            print(nom_region)

    def test_afficher_les_departements_de_chaque_region_pour_annuaire_service_public(self):
        print("test_afficher_les_departements_de_chaque_region_pour_annuaire_service_public")

        url_regions = "https://geo.api.gouv.fr/regions?fields=code,nom,codeDepartement&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url_regions, headers=headers, data=payload)

        regions = json.loads(response.text)

        for region in regions:
            code_region = str(region['code'])
            nom_region = region['nom'].lower()\
                .replace('î', 'i')\
                .replace('é', 'e')\
                .replace('è', 'e')\
                .replace('à', 'a')\
                .replace('ô', 'o')\
                .replace("'", '-')\
                .replace(' ', '-')

            url_departements = "https://geo.api.gouv.fr/regions/" + code_region + "/departements?fields=code,nom,codeRegion,region&format=json"

            payload = {}
            headers = {}

            response = requests.request("GET", url_departements, headers=headers, data=payload)

            departements = json.loads(response.text)

            for departement in departements:
                nom_departement = departement['nom'].lower()\
                    .replace('î', 'i')\
                    .replace('é', 'e')\
                    .replace('è', 'e')\
                    .replace('à', 'a')\
                    .replace('ô', 'o')\
                    .replace("'", '-')\
                    .replace(' ', '-')
                print("region : " + nom_region + " - departement : " + nom_departement)

    def test_afficher_les_code_insee_communes_de_chaque_departement_pour_annuaire_service_public(self):
        print("test_afficher_les_code_insee_communes_de_chaque_departement_pour_annuaire_service_public")

        url_regions = "https://geo.api.gouv.fr/regions?fields=code,nom,codeDepartement&format=json"

        payload = {}

        headers = {}

        response = requests.request("GET", url_regions, headers=headers, data=payload)

        regions = json.loads(response.text)

        for region in regions:
            code_region = str(region['code'])

            nom_region = region['nom'].lower()\
                .replace('î', 'i')\
                .replace('é', 'e')\
                .replace('è', 'e')\
                .replace('à', 'a')\
                .replace('ô', 'o')\
                .replace("'", '-')\
                .replace(' ', '-')

            url_departements = "https://geo.api.gouv.fr/regions/" + code_region + "/departements?fields=code,nom,codeRegion,region&format=json"

            payload = {}

            headers = {}

            response = requests.request("GET", url_departements, headers=headers, data=payload)

            departements = json.loads(response.text)

            for departement in departements:
                code_departement = departement['code']

                nom_departement = departement['nom'].lower()\
                    .replace('î', 'i')\
                    .replace('é', 'e')\
                    .replace('è', 'e')\
                    .replace('à', 'a')\
                    .replace('ô', 'o')\
                    .replace("'", '-')\
                    .replace(' ', '-')

                url_communes = "https://geo.api.gouv.fr/departements/" + code_departement + "/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

                payload = {}

                headers = {}

                response = requests.request("GET", url_communes, headers=headers, data=payload)

                communes = json.loads(response.text)

                for commune in communes:
                    code_insee_commune = commune['code']

                    print("region : " + nom_region
                          + " - departement : " + nom_departement
                          + " - code insee commune : " + code_insee_commune)

    def test_recuperer_les_informations_concernant_une_region(self):
        print("test_recuperer_les_informations_concernant_une_region")

        url = "https://geo.api.gouv.fr/regions/11?fields=code,nom&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_recuperer_le_nom_concernant_une_region(self):
        print("test_recuperer_les_informations_concernant_une_region")

        url = "https://geo.api.gouv.fr/regions/11?fields=code,nom&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        nomRegion = json.loads(response.text)["nom"]

        print(nomRegion)

    def test_communes_avec_moins_de_1000_habitants(self):
        print("test_communes_avec_moins_de_1000_habitants")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        communes = response.json()

        for commune in communes:
            try:
                if commune['population'] < 1000:
                    print(commune)
            except Exception as e:
                print("error : " + str(e))

    def test_communes_avec_plus_de_20000_habitants(self):
        print("test_communes_avec_plus_de_20000_habitants")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        communes = response.json()

        for commune in communes:
            try:
                if commune['population'] > 20000:
                    print(commune['nom'].lower()
                          .replace(' ', '-')
                          .replace('ê', 'e')
                          .replace('é', '')
                          .replace('è', '')
                          .replace('à', 'a')
                          .replace('â', 'a')
                          .replace('ô', 'o')
                          )
            except Exception as e:
                print("error : " + str(e))

    def test_afficher_code_insee_communes_avec_moins_de_1000_habitants(self):
        print("test_afficher_code_insee_communes_avec_moins_de_1000_habitants")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        communes = response.json()

        for commune in communes:
            try:
                if commune['population'] < 1000:
                    print(" code insee : " + commune['code'])
            except Exception as e:
                print("error : " + str(e))

    def test_afficher_code_departement_avec_des_communes_avec_moins_de_1000_habitants(self):
        print("test_afficher_code_insee_communes_avec_moins_de_1000_habitants")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        communes = response.json()

        for commune in communes:
            try:
                if commune['population'] < 1000:
                    print(" code insee departement : " + commune['codeDepartement'])
            except Exception as e:
                print("error : " + str(e))


# https://geo.api.gouv.fr/adresse
class UnitTestsGeoApiGouvFrAdresse(unittest.TestCase):
    # Point d’entrée pour le géocodage.
    def test_search(self):
        print('test_search')

        url = "https://api-adresse.data.gouv.fr/search/?q=8+bd+du+port"

        payload = {}

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        json_format = json.loads(response.text)

        print(json_format)

    # Point d’entrée pour le géocodage inverse.
    def test_reverse(self):
        print('test_search')

        lon = "2.03349"

        lat = "49.04986"

        url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

        # payload = {}

        # headers = {}

        # response = requests.request("GET", url, headers=headers, data=payload)
        response = requests.request("GET", url)

        json_format = json.loads(response.text)

        print(json_format)

    # Point d’entrée pour le géocodage inverse pour le code insee commune
    def test_reverse_pour_code_insee_commune(self):
        print('test_reverse_pour_code_insee_commune')

        lon = "2.03349"

        lat = "49.04986"

        url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

        response = requests.request("GET", url)

        json_format = json.loads(response.text)

        code_insee_commune = json_format['features'][0]['properties']['citycode']

        code_insee_departement = code_insee_commune[:2]

        print('code_insee_commune : ' + str(code_insee_commune)
              + " _ code_insee_departement : " + str(code_insee_departement))

    # Point d’entrée pour le géocodage inverse sur plusieurs
    def test_display_all_postal_addresses(self):
        print('test_display_all_postal_addresses')

        lon = "2.03349"

        lat = "49.04986"

        url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

        payload = {}

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        json_format = json.loads(response.text)

        for feature in json_format['features']:
            print(feature['properties']['label'])

    # Afficher le nombre d'éléments des coordonnées
    def test_length_elements(self):
        print('test_length_elements')

        coordinates = [[[4.9258823,46.1769605],[4.9230879,46.1773166],[4.9230816,46.1772642],[4.9258656,46.1769041],[4.9258823,46.1769605]]]

        print('length coordinates : ' + str(len(coordinates[0])))

    # Point d’entrée pour le géocodage inverse depuis coordinates parcelles
    def test_reverse_coordinates_parcelles(self):
        print('test_reverse_coordinates_parcelles')

        coordinates = [[[4.9258823,46.1769605],[4.9230879,46.1773166],[4.9230816,46.1772642],[4.9258656,46.1769041],[4.9258823,46.1769605]]]

        for coordinate in coordinates[0]:
            lon = str(coordinate[0])

            lat = str(coordinate[1])

            url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

            payload = {}

            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            json_format = json.loads(response.text)

            if len(json_format['features']) != 0:
                print("coordinate : " + lon + " _ " + lat + str(json_format))
                break


# https://api.gouv.fr/documentation/api_carto_gpu
class UnitTestsApiGouvFrApiCartoGpu(unittest.TestCase):
    def test_convert_geometry(self):
        actual = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        expected = '%7B%22type%22%3A%20%22Point%22%2C%20%22coordinates%22%3A%20%5B2.03349%2C%2049.04986%5D%7D'

        self.assertEqual(actual, expected)

    # Récupération des informations sur une commune (est au RNU? est supprimée?)
    def test_gpu_municipality(self):
        print("test_gpu_municipality")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/municipality'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération de l'emprise d'un document
    def test_gpu_document(self):
        print("test_gpu_document")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/document'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        json_format = json.loads(response.text)

        print(json_format)

    # Récupération des zonages d’un document d’urbanisme
    def test_gpu_zone_urba_for_one_point(self):
        print("test_gpu_zone_urba_for_one_point")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/zone-urba'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des zonages d’un document d’urbanisme
    def test_gpu_zone_urba_for_several_point(self):
        print("test_gpu_zone_urba_for_several_point")

        f = open('cadastre-01001-parcelles.json', "r")

        data = json.loads(f.read())

        for feature in data['features']:
            prefixe = feature['properties']['prefixe']
            section = feature['properties']['section']
            numero = feature['properties']['numero']
            point = feature['geometry']['coordinates'][0][0]

            geometry = '{"type": "Point", "coordinates": ' + str(point) + '}' \
                .replace('{', '%7B') \
                .replace('"', '%22') \
                .replace(':', '%3A') \
                .replace(' ', '%20') \
                .replace(',', '%2C') \
                .replace(' ', '%20') \
                .replace('[', '%5B') \
                .replace(']', '%5D') \
                .replace('}', '%7D')

            base_url = 'https://apicarto.ign.fr/api'

            api = '/gpu/zone-urba'

            url = base_url + api + '?geom=' + geometry

            payload = {}

            headers = {}

            response = requests.get(url, headers=headers, data=payload)

            data_response = json.loads(response.text)

            features1 = data_response['features']

            print("point : " + str(point))

            if len(features1) >= 1:
                for feature1 in features1:
                    libelle = feature1['properties']['libelle']
                    libelong = feature1['properties']['libelong']

                    print('parcelle cadastrale : ' + str(prefixe + section + numero) + 'de type '
                          + str(libelle) + ' - ' + str(libelong))

        f.close()

    # Récupération des zonages d’un document d’urbanisme
    def test_gpu_zone_urba_for_one_multiPolygon(self):
        print("test_gpu_zone_urba_for_one_multiPolygon")

        geometry = '{"type":"MultiPolygon","coordinates":[[[[4.9259873,46.1772431],[4.92608,46.1774442],' \
                   '[4.9260901,46.1774537],[4.9231649,46.1776782],[4.9231363,46.1775902],[4.9231171,46.1774918],' \
                   '[4.9231037,46.1774118],[4.9230879,46.1773166],[4.9258823,46.1769605],[4.925903,46.1770116],' \
                   '[4.9259387,46.177106],[4.9259873,46.1772431]]]]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/zone-urba'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des secteurs d’une carte communale
    def test_gpu_secteur_cc(self):
        print("test_gpu_secteur_cc")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/secteur-cc'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des prescriptions surfaciques d’un document d’urbanisme
    def test_gpu_prescription_surf(self):
        print("test_gpu_prescription_surf")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/prescription-surf'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des prescriptions linéaires d’un document d’urbanisme
    def test_gpu_prescription_lin(self):
        print("test_gpu_prescription_lin")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/prescription-lin'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des prescriptions ponctuelles d’un document d’urbanisme
    def test_gpu_prescription_pct(self):
        print("test_gpu_prescription_pct")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/prescription-pct'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des informations surfaciques d’un document d’urbanisme
    def test_gpu_info_surf(self):
        print("test_gpu_info_surf")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/info-surf'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des informations linéaires d’un document d’urbanisme
    def test_gpu_info_lin(self):
        print("test_gpu_info_lin")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/info-lin'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des informations ponctuelles d’un document d’urbanisme
    def test_gpu_info_pct(self):
        print("test_gpu_info_pct")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/info-pct'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des actes des servitudes d’utilité publique
    def test_gpu_acte_sup(self):
        print("test_gpu_acte_sup")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/acte-sup'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des assiettes surfaciques de servitudes d’utilité publique
    def test_gpu_assiette_sup_s(self):
        print("test_gpu_assiette_sup_s")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/assiette-sup-s'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des assiettes linéaires de servitudes d’utilité publique
    def test_gpu_assiette_sup_l(self):
        print("test_gpu_assiette_sup_l")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/assiette-sup-l'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des assiettes ponctuelles de servitudes d’utilité publique
    def test_gpu_assiette_sup_p(self):
        print("test_gpu_assiette_sup_p")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/assiette-sup-p'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des générateurs surfaciques des servitudes d’utilité publique
    def test_gpu_generateur_sup_s(self):
        print("test_gpu_generateur_sup_s")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/generateur-sup-s'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des générateurs linéaires des servitudes d’utilité publique
    def test_gpu_generateur_sup_l(self):
        print("test_gpu_generateur_sup_l")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/generateur-sup-l'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération des générateurs ponctuels des servitudes d’utilité publique
    def test_gpu_generateur_sup_p(self):
        print("test_gpu_generateur_sup_p")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/generateur-sup-p'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Récupération de l’ensemble des couches décrites ci-dessus
    def test_gpu_all(self):
        print("test_gpu_all")

        geometry = '{"type": "Point", "coordinates": [2.03349, 49.04986]}' \
            .replace('{', '%7B') \
            .replace('"', '%22') \
            .replace(':', '%3A') \
            .replace(' ', '%20') \
            .replace(',', '%2C') \
            .replace(' ', '%20') \
            .replace('[', '%5B') \
            .replace(']', '%5D') \
            .replace('}', '%7D')

        base_url = 'https://apicarto.ign.fr/api'

        api = '/gpu/all'

        url = base_url + api + '?geom=' + geometry

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))


# https://www.geoportail-urbanisme.gouv.fr/api/#/Documents/get-documents
class UnitTestsApiGeoportailUrbanisme(unittest.TestCase):
    # Renvoie une liste de documents filtrées en fonction des paramètres.
    def test_document(self):
        print("test_gpu_municipality")

        base_url = 'https://www.geoportail-urbanisme.gouv.fr/api'

        api = '/document'

        url = base_url + api

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        print(json.loads(response.text))

    # Renvoie les informations détaillées sur un document.
    def test_document_id_details(self):
        print("test_gpu_municipality")

        base_url = 'https://www.geoportail-urbanisme.gouv.fr/api'

        api = '/document/'

        id = '531f797f5254fc05948953e332d2742f'

        url = base_url + api + id + '/details'

        payload = {}

        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        json_format = json.loads(response.text)

        print(json_format)


if __name__ == '__main__':
    unittest.main()
