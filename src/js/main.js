import { setupCounter } from "./counter.js";
import { callApi1, callApi2 } from "./testAPI.js";

setupCounter(document.querySelector("#counter"));

callApi1();
callApi2();
