import streamlit as st

# Komponentit ja kuvaukset
komponentit = {
    "energia": "Ruoasta saatava kokonaisenergiamäärä, mitattuna kilokaloreina tai kilojouleina.",
    "rasva": "Makroravinne, joka toimii energianlähteenä ja solujen rakennusaineena.",
    "hiilihydraatti imeytyvä": "Hiilihydraatti, joka imeytyy suolistossa ja nostaa verensokeria.",
    "proteiini": "Makroravinne, joka rakentaa ja korjaa kudoksia, erityisen tärkeä ikäihmisille.",
    "alkoholi": "Energiapitoinen yhdiste, ei suositeltava ravinnonlähde.",
    "orgaaniset hapot": "Luonnollisia happoja, jotka vaikuttavat makuun ja aineenvaihduntaan.",
    "sokerialkoholit": "Makeuttajia, joilla on vähemmän energiaa kuin tavallisilla sokereilla.",
    "sokerit": "Yksinkertaisia hiilihydraatteja, kuten glukoosi ja fruktoosi.",
    "fruktoosi": "Hedelmissä esiintyvä sokeri.",
    "galaktoosi": "Sokeri, jota esiintyy mm. laktoosissa.",
    "glukoosi": "Verensokeri, tärkein solujen energianlähde.",
    "laktoosi": "Maitosokeri, koostuu glukoosista ja galaktoosista.",
    "maltoosi": "Kahden glukoosimolekyylin muodostama sokeri.",
    "sakkaroosi": "Tavallinen ruokasokeri, glukoosi + fruktoosi.",
    "tärkkelys": "Pitkäketjuinen hiilihydraatti, tärkeä energianlähde.",
    "kuitu,-kokonais": "Ruoansulatusta edistävä hiilihydraatti, ei imeydy.",
    "kuitu, veteen liukenematon": "Kuitu, joka lisää ulostemassaa ja ehkäisee ummetusta.",
    "polysakkaridi, vesiliukoinen ei sellukoosa": "Liukoinen kuitu, joka vaikuttaa kolesteroliin ja verensokeriin.",
    "rasvahapot yhteensä": "Kaikki rasvahapot, mukaan lukien tyydyttyneet ja tyydyttymättömät.",
    "rasvahapot monityydyttämättömät": "Hyödyllisiä rasvahappoja, kuten omega-3 ja omega-6.",
    "rasvahapot yksittäistyydyttymättömät cis": "Esim. oliiviöljyn rasvahapot, sydänystävällisiä.",
    "rasvahapot tyydyttyneet": "Rasvahapot, joiden runsas saanti voi nostaa kolesterolia.",
    "rasvahapot trans": "Teollisesti muodostuneet rasvahapot, haitallisia terveydelle.",
    "rasvahapot n-3 monityydyttämättömät": "Omega-3-rasvahapot, kuten EPA ja DHA.",
    "rasvahapot n-6 monityydyttämättömät": "Omega-6-rasvahapot, joita saadaan kasviöljyistä.",
    "rasvahappo 18:2 cis,cis n-6 (linolihappo)": "Välttämätön omega-6-rasvahappo.",
    "rasvahappo 18:3 n-3 (alfalinoleenihappo)": "Kasviperäinen omega-3-rasvahappo.",
    "rasvahappo 20:5 n-3 (EPA)": "Kalaöljyistä saatava omega-3-rasvahappo.",
    "rasvahappo 22:6 n-3 (DHA)": "Aivojen ja näön kehitykselle tärkeä omega-3-rasvahappo.",
    "kolesteroli (GC)": "Rasvayhdiste, jota elimistö tarvitsee mutta liika voi olla haitallista.",
    "sterolit": "Kasviperäisiä yhdisteitä, jotka voivat alentaa kolesterolia.",
    "kalsium": "Luuston rakennusaine, tärkeä myös hermoston toiminnalle.",
    "rauta": "Välttämätön veren hemoglobiinin muodostumiselle.",
    "jodidi (jodi)": "Kilpirauhasen toiminnalle tärkeä hivenaine.",
    "kalium": "Säätelee nestetasapainoa ja verenpainetta.",
    "magnesium": "Osallistuu yli 300 entsyymireaktioon elimistössä.",
    "natrium": "Säätelee nestetasapainoa, liiallinen saanti nostaa verenpainetta.",
    "suola": "Natriumin lähde, liiallinen saanti on yleistä.",
    "fosfori": "Luuston ja solujen rakennusaine.",
    "seleeni": "Antioksidanttina toimiva hivenaine.",
    "sinkki": "Tärkeä immuunijärjestelmälle ja haavojen paranemiselle.",
    "tryptofaani": "Aminohappo, joka on serotoniinin esiaste.",
    "folaatti, kokonais-": "Solujen jakautumiseen ja DNA-synteesiin tarvittava vitamiini.",
    "niasiiniekvivalentti NE": "B3-vitamiinin kokonaismäärä eri lähteistä.",
    "niasiini (nikotiinihappo + nikotiiniamidi)": "B3-vitamiini, tärkeä energiantuotannossa.",
    "pyridoksiini vitameerit (vetykloridi) (B6)": "B6-vitamiini, tärkeä proteiiniaineenvaihdunnassa.",
    "riboflaviini (B2)": "B2-vitamiini, osallistuu energiantuotantoon.",
    "tiamiini (B1)": "B1-vitamiini, tärkeä hermoston toiminnalle.",
    "A-vitamiini RAE": "Näkökyvyn ja solujen kasvun kannalta tärkeä vitamiini.",
    "karotenoidit": "A-vitamiinin esiasteita, antioksidanttisia yhdisteitä.",
    "B12-vitamiini (kobalamiini)": "Hermoston ja veren muodostuksen kannalta välttämätön.",
    "C-vitamiini": "Antioksidantti, edistää raudan imeytymistä.",
    "D-vitamiini": "Säätelee kalsiumin imeytymistä, tärkeä luustolle ja immuunipuolustukselle.",
    "E-vitamiini alfatokoferoli": "Antioksidantti, suojaa soluja hapettumiselta.",
    "K-vitamiini": "Tarvitaan veren hyytymiseen ja luuston aineenvaihduntaan."
}

st.title("🧬 Ravintokomponenttien hakukone")

with st.expander("📋 Näytä kaikki komponentit"):
    valinta = st.selectbox("Valitse komponentti", list(komponentit.keys()))
    if valinta:
        st.subheader(f"🧾 {valinta.capitalize()}")
        st.write(komponentit[valinta])

st.markdown("---")
st.caption("Tietolähde: komponentit-data2.pdf")
