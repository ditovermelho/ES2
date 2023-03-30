//import GetCustomer from "./scenarios/Get-Customer.js";
import sigleRequest from "./scenarios/sigle-request.js";
import { group, sleep } from "k6";

export default () => {
    /*group('Endpoit Get Customer - Controller Customer - OnionArchitecture.Api', () => {
        GetCustomer();
    }) */

    group('Endpoit sigleResquest - Controller Customer - OnionArchitecture.Api', () =>{
        sigleRequest();
    })

    sleep(1);
}