import http from "k6/http";
import { sleep, check } from "k6";

export const options = { vus : 1, duration: "10s" };
const url = "https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api";

export default function() {

    const params = {
        headers: {
            'x-api-key': '75833cf59bc93ea84745f49cb713319f680b03053cc365be0fa116d8883d1b66',
            "Content-Type": "application/json",
        },};
        
        

    const payload = JSON.stringify({
        first_name: "Ali",
        last_name: "Test",
        personal_number: "19900101-1234",
        email: "ali@test.se",
        loan_amount: 10000,
        address: "Testgatan 1",
        postcode: "12345",
        city: "Stockholm",
        phone: "0701234567",
        employment_type: "employed",
        employer: "Test AB",
        income: 30000,
        repayment_months: 12,
        product_type: "personal"
    });

        const response = http.post(url, payload, params);

        check(response, {
            "status is 200": (r) => r.status === 200,
        'response time < 100ms': (r) => r.timings.duration < 300,
        'response time < 500ms': (r) => r.timings.duration < 500,
        'response time < 200ms': (r) => r.timings.duration < 700,
        'response time < 300ms': (r) => r.timings.duration < 850,
        'response time < 100ms': (r) => r.timings.duration < 1000,
    });
    console.log("STATUS:", response.status);
    /*console.log("BODY:", response.body);*/
    sleep(1);
}
