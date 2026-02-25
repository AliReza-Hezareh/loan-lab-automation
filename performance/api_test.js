import http from "k6/http";
import { sleep, check } from "k6";

export const options = { vus : 10, duration: "30s" };

export default function() {
    const url = "https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api"

    const params = {
        headers: {
            'xapi-key': '75833cf59bc93ea84745f49cb713319f680b03053cc365be0fa116d8883d1b66,4c13d26460527b2c6e9ecc3370a65330cf3a431b97dc9ad4724a88a00ba4d76d ',
        },};
        const response = http.get(url, params);

        check(response, {
            "status is 200": (r) => r.status === 200,
        
        'response time < 500ms': (r) => r.timings.duration < 500,
        'response time < 200ms': (r) => r.timings.duration < 200,
        'response time < 100ms': (r) => r.timings.duration < 100,
    });
    sleep(1);
}
