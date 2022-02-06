import unittest
import requests


# https://opendata.reseaux-energies.fr/explore/?disjunctive.theme&disjunctive.publisher&disjunctive.maille-geographique&disjunctive.frequence-de-mise-a-jour&disjunctive.pas-temporel&sort=modified&refine.energie=Gaz
class UnitTestsAPIOpenDataReseauxEnergiesGaz(unittest.TestCase):
    def test_programme_travaux_communs_des_operateurs_gaziers(self):
        print('test_programme_travaux_communs_des_operateurs_gaziers')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=programme-travaux-communs-des-operateurs-gaziers-annee-2020-2021&q=&facet=date&facet=label_pcr&facet=id_points_dinteret&facet=operateur&facet=sens_du_flux&facet=storage&facet=valeur_nulle"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/registre-des-emissions-polluantes/api/?disjunctive.polluant&disjunctive.commune&disjunctive.departement&disjunctive.region
    def test_registre_des_emissions_polluantes(self):
        print('test_registre_des_emissions_polluantes')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=registre-des-emissions-polluantes&q=&facet=annee_emission&facet=milieu&facet=polluant&facet=commune&facet=departement&facet=region"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/consommation-quotidienne-brute/api/
    def test_consommation_quotidienne_brute(self):
        print('test_consommation_quotidienne_brute')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=consommation-quotidienne-brute&q=&facet=date_heure&facet=date&facet=heure&facet=statut_grtgaz&facet=statut_rte"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/consommation-quotidienne-brute-regionale/information/?disjunctive.code_insee_region&disjunctive.region
    def test_consommation_quotidienne_brute_regionale(self):
        print('test_consommation_quotidienne_brute_regionale')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=consommation-quotidienne-brute-regionale&q=&facet=date_heure&facet=code_insee_region&facet=region"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/points-dinjection-de-biomethane-en-france/information/?disjunctive.site&disjunctive.nom_epci&disjunctive.departement&disjunctive.region&disjunctive.type_de_reseau&disjunctive.grx_demandeur
    def test_points_dinjection_de_biomethane_en_france(self):
        print('test_points_dinjection_de_biomethane_en_france')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=points-dinjection-de-biomethane-en-france&q=&facet=site&facet=commune&facet=nom_epci&facet=departement&facet=region&facet=annee_mes&facet=type_de_reseau&facet=grx_demandeur"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/evolution-de-la-consommation-de-gnl-carburant-routier/api/
    def test_evolution_de_la_consommation_de_gnl_carburant_routier(self):
        print('test_evolution_de_la_consommation_de_gnl_carburant_routier')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=evolution-de-la-consommation-de-gnl-carburant-routier&q="

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/conversion-des-unites-gazieres/api/
    def test_conversion_des_unites_gazieres(self):
        print('test_conversion_des_unites_gazieres')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=conversion-des-unites-gazieres&q="

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/previsions-des-capacites-dapprovisionnement-de-leurope-a-horizon-2030/api/
    def test_previsions_des_capacites_dapprovisionnement_de_leurope_a_horizon_2030(self):
        print('test_previsions_des_capacites_dapprovisionnement_de_leurope_a_horizon_2030')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=previsions-des-capacites-dapprovisionnement-de-leurope-a-horizon-2030&q="

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/installations-regionales-de-biomethane/api/?disjunctive.region
    def test_installations_regionales_de_biomethane(self):
        print('test_installations_regionales_de_biomethane')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=installations-regionales-de-biomethane&q=&facet=date&facet=region"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/potentiel-national-production-methane-renouvelable-gazeification-hydrothermale/information/?disjunctive.famille_de_dechets&disjunctive.typologie_de_dechets
    def test_potentiel_national_production_methane_renouvelable_gazeification_hydrothermale(self):
        print('test_potentiel_national_production_methane_renouvelable_gazeification_hydrothermale')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=potentiel-national-production-methane-renouvelable-gazeification-hydrothermale&q=&facet=famille_de_dechets&facet=typologie_de_dechets"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/production-nationale-horaire-de-gaz-donnees-definitives/information/
    def test_production_nationale_horaire_de_gaz_donnees_definitives(self):
        print('test_production_nationale_horaire_de_gaz_donnees_definitives')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=production-nationale-horaire-de-gaz-donnees-definitives&q=&facet=annee_mois&facet=journee_gaziere"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/production-mensuelle-biomethane/information/
    def test_production_mensuelle_biomethane(self):
        print('test_production_mensuelle_biomethane')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=production-mensuelle-biomethane&q=&facet=annee&facet=mois"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/trace-du-reseau-grt-250/information/
    def test_trace_du_reseau_grt_250(self):
        print('test_trace_du_reseau_grt_250')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=trace-du-reseau-grt-250&q=&facet=nom_region&facet=departement_concerne"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/sites-rebours-grtgaz/information/?disjunctive.donnees_rebours_nom_du_projet&disjunctive.nom_de_la_region&disjunctive.nom_du_departement
    def test_sites_rebours_grtgaz(self):
        print('test_sites_rebours_grtgaz')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=sites-rebours-grtgaz&q=&facet=donnees_rebours_nom_du_projet&facet=mes_dpi_agora&facet=horizon_de_saturation&facet=validation_cre&facet=nom_de_la_region&facet=nom_du_departement"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/joint-maintenance-schedule-of-french-gas-operators-for-the-period-20202021/information/?disjunctive.calendar_date
    def test_joint_maintenance_schedule_of_french_gas_operators_for_the_period_20202021(self):
        print('test_joint_maintenance_schedule_of_french_gas_operators_for_the_period_20202021')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=joint-maintenance-schedule-of-french-gas-operators-for-the-period-20202021&q=&facet=calendar_date&facet=point_dinteret&facet=id_points_dinterets&facet=operateur&facet=sens_du_flux&facet=valeur_null"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/vol-echange-gaz-eu/information/?disjunctive.annee
    def test_vol_echange_gaz_eu(self):
        print('test_vol_echange_gaz_eu')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=vol-echange-gaz-eu&q=&facet=annee"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/conso-journa-industriel-grtgazterega/information/?disjunctive.operateur&disjunctive.region
    def test_conso_journa_industriel_grtgazterega(self):
        print('test_conso_journa_industriel_grtgazterega')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=conso-journa-industriel-grtgazterega&q=&facet=date&facet=operateur&facet=region"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/consommation-annuelle-par-iris/information/?disjunctive.hierarchie_geographique
    def test_consommation_annuelle_par_iris(self):
        print('test_consommation_annuelle_par_iris')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=consommation-annuelle-par-iris&q=&facet=annee&facet=hierarchie_geographique"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/conso-gaz-metropole/information/?disjunctive.nom_officiel_epci
    def test_conso_gaz_metropole(self):
        print('test_conso_gaz_metropole')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=conso-gaz-metropole&q=&facet=date&facet=nom_officiel_epci&facet=region"

        response = requests.request("GET", url)

        print(response.json())

    # https://opendata.reseaux-energies.fr/explore/dataset/production-nationale-horaire-de-gaz-donnees-provisoires/information/
    def test_production_nationale_horaire_de_gaz_donnees_provisoires(self):
        print('test_production_nationale_horaire_de_gaz_donnees_provisoires')

        endpoint = "https://opendata.reseaux-energies.fr"

        url = endpoint + "/api/records/1.0/search/?dataset=production-nationale-horaire-de-gaz-donnees-provisoires&q=&facet=date"

        response = requests.request("GET", url)

        print(response.json())


if __name__ == '__main__':
    unittest.main()
