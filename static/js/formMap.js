async function initMap() {
    // Request needed libraries.
    const {Map} = await google.maps.importLibrary("maps");
    const {AdvancedMarkerElement} = await google.maps.importLibrary("marker");

    const directionsRenderer = new google.maps.DirectionsRenderer();
    const directionsService = new google.maps.DirectionsService();


    const map = new Map(document.getElementById("map"), {
        center: {lat: 44.9727, lng: -93.23540000000003},
        zoom: 15,
        mapId: "DEMO_MAP_ID",
    });
    directionsRenderer.setMap(map);
    directionsRenderer.setPanel(document.getElementById("navBar"));

    const marker = new AdvancedMarkerElement({
        map,
        position: {lat: 44.9727, lng: -93.23540000000003},
    });
    async function autoComplete(){
        const input = document.getElementById('location');
        const { Autocomplete } = await google.maps.importLibrary('places');
        const autocomplete = new Autocomplete(input);
        autocomplete.addListener("place_changed", () => {
            document.getElementById("navBar").style.visibility="visible";
            const start=document.getElementById("location").value;
            const end = "1901 4th St SE, Minneapolis, MN 55455";
            const mode = "DRIVING";
            directionsService
                .route({
                    origin: start,
                    destination: end,
                    travelMode: google.maps.TravelMode[mode],
                })
                .then((response) => {
                    directionsRenderer.setDirections(response);
                })//source: https://console.cloud.google.com/google/maps-apis/discover/text-directions?project=crucial-guard-488717-n0
        });
    }
    await autoComplete();
}
initMap();