
async function initMap() {
    // Request needed libraries.
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
    const map = new Map(document.getElementById("map"), {
        center: {lat: 44.9727, lng: -93.23540000000003},
        zoom: 15,
        mapId: "DEMO_MAP_ID",
    });

    const marker = new AdvancedMarkerElement({
        map,
        position: {lat:44.9727, lng: -93.23540000000003},
    });
    //populates addressList with addresses from table (not limited by hardcoded table length)
    //then converts to a location using geocoder and makes a new marker
    async function addressesToMarker() {
        let addressList = [];
        const data = document.querySelectorAll("#guest-table td");
        for (let i = 3; i < data.length; i += 6) {
            addressList.push(data[i].innerHTML.match(/^[^<]+/)[0].trim());
        }
        let nameList=[];
        for(let i = 0; i< data.length;i+=6){
            nameList.push(data[i].innerHTML);
        }
        let phoneList = [];
        for(let i = 4; i< data.length;i+=6){
            phoneList.push(data[i].innerHTML);
        }

        const {Place} = await google.maps.importLibrary("places");
        for (let i = 0;i<addressList.length;i++){
            const request = {
                textQuery: addressList[i],
                fields: ["location"],
            };
            const {places} = await Place.searchByText(request);
            if (places.length > 0) {
                const infoWindow = new google.maps.InfoWindow({
                    content: `<div>
                        <h1>${nameList[i]}</h1>
                        ${addressList[i]}<br>
                        ${phoneList[i]}
                        </div>`,
                });
                const position = places[0].location;
                const marker = new AdvancedMarkerElement({
                    map,
                    position: position,
                });
                marker.addListener("click", () => {
                    infoWindow.open(map, marker);
                });
            }
        }
    }

await addressesToMarker();
}

initMap();
