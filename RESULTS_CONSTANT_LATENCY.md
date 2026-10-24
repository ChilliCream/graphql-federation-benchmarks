## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-net-11 | 16.7.0-p.38 | 2,771 | 2,868 | 2,760 | 1.3% |  |
| fusion-nightly-net-10 | 16.7.0-p.38 | 2,748 | 2,854 | 2,726 | 1.5% |  |
| fusion-nightly-aot-11 | 16.7.0-p.38 | 2,725 | 2,817 | 2,688 | 1.5% |  |
| fusion-nightly-fed-net-11 | 16.7.0-p.38 | 2,472 | 2,547 | 2,451 | 1.3% |  |
| feddi-gateway | 3c75a7db8876 | 2,469 | 2,575 | 2,453 | 1.6% |  |
| fusion-nightly-fed-aot-11 | 16.7.0-p.38 | 2,439 | 2,515 | 2,425 | 1.1% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.38 | 2,438 | 2,523 | 2,407 | 1.6% |  |
| fusion-net-11 | 16.6.9 | 1,908 | 1,955 | 1,901 | 0.9% |  |
| fusion-net-10 | 16.6.9 | 1,889 | 1,936 | 1,874 | 1.1% |  |
| hive-router | v0.3.5 | 1,856 | 1,928 | 1,847 | 1.5% |  |
| fusion-aot-11 | 16.6.9 | 1,835 | 1,883 | 1,829 | 1.0% |  |
| fusion-fed-net-10 | 16.6.9 | 1,826 | 1,878 | 1,815 | 1.1% |  |
| fusion-fed-net-11 | 16.6.9 | 1,823 | 1,879 | 1,808 | 1.3% |  |
| fusion-fed-aot-11 | 16.6.9 | 1,756 | 1,800 | 1,741 | 1.1% |  |
| grafbase | 0.53.5 | 1,320 | 1,345 | 1,315 | 0.9% |  |
| cosmo | 0.361.0 | 1,302 | 1,359 | 1,292 | 1.7% |  |
| caliban | 3.2.0 | 1,280 | 1,340 | 1,274 | 1.9% |  |
| hive-gateway-router-runtime | 2.15.2 | 505 | 519 | 502 | 1.2% |  |
| apollo-router | v2.18.0 | 397 | 416 | 394 | 1.9% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 368 | 384 | 366 | 1.9% |  |
| apollo-gateway | 2.14.4 | 262 | 266 | 260 | 0.8% |  |
| hive-gateway | 2.15.2 | 260 | 268 | 259 | 1.2% |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1005801     ✗ 0     
     data_received..................: 29 GB   243 MB/s
     data_sent......................: 403 MB  3.3 MB/s
     http_req_blocked...............: avg=3.09µs   min=802ns   med=1.78µs  max=17.24ms  p(90)=3.15µs  p(95)=4.07µs  p(99.9)=25.93µs
     http_req_connecting............: avg=725ns    min=0s      med=0s      max=7.99ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.68ms  min=8.64ms  med=16.85ms max=291.42ms p(90)=22.96ms p(95)=25.57ms p(99.9)=46.63ms
       { expected_response:true }...: avg=17.68ms  min=8.64ms  med=16.85ms max=291.42ms p(90)=22.96ms p(95)=25.57ms p(99.9)=46.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 335367
     http_req_receiving.............: avg=714.87µs min=49.23µs med=82.26µs max=279.09ms p(90)=2.35ms  p(95)=3.79ms  p(99.9)=23.15ms
     http_req_sending...............: avg=44.48µs  min=4.35µs  med=7.42µs  max=178.17ms p(90)=16.48µs p(95)=83.9µs  p(99.9)=5.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=16.92ms  min=8.34ms  med=16.11ms max=265.3ms  p(90)=21.79ms p(95)=24.43ms p(99.9)=44.2ms 
     http_reqs......................: 335367  2771.56839/s
     iteration_duration.............: avg=17.88ms  min=8.83ms  med=17.04ms max=304.94ms p(90)=23.16ms p(95)=25.79ms p(99.9)=47.17ms
     iterations.....................: 335267  2770.741961/s
     success_rate...................: 100.00% ✓ 335267      ✗ 0     
     vus............................: 47      min=47        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 997323      ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=2.48µs  min=832ns   med=1.77µs  max=9.27ms   p(90)=3.04µs  p(95)=3.95µs  p(99.9)=25.42µs
     http_req_connecting............: avg=306ns   min=0s      med=0s      max=4.24ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.83ms min=8.63ms  med=17.02ms max=279.94ms p(90)=23.08ms p(95)=25.76ms p(99.9)=47.91ms
       { expected_response:true }...: avg=17.83ms min=8.63ms  med=17.02ms max=279.94ms p(90)=23.08ms p(95)=25.76ms p(99.9)=47.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 332541
     http_req_receiving.............: avg=770.3µs min=49.79µs med=82.89µs max=201.34ms p(90)=2.52ms  p(95)=3.89ms  p(99.9)=24.07ms
     http_req_sending...............: avg=43.2µs  min=4.23µs  med=7.47µs  max=59.72ms  p(90)=15.92µs p(95)=83.78µs p(99.9)=5.18ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.02ms min=8.52ms  med=16.19ms max=276.86ms p(90)=21.99ms p(95)=24.61ms p(99.9)=45.45ms
     http_reqs......................: 332541  2748.110892/s
     iteration_duration.............: avg=18.04ms min=8.79ms  med=17.21ms max=301.71ms p(90)=23.28ms p(95)=25.99ms p(99.9)=48.28ms
     iterations.....................: 332441  2747.284495/s
     success_rate...................: 100.00% ✓ 332441      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 989355      ✗ 0     
     data_received..................: 29 GB   239 MB/s
     data_sent......................: 396 MB  3.3 MB/s
     http_req_blocked...............: avg=2.63µs   min=811ns   med=1.76µs  max=12.08ms  p(90)=3.1µs   p(95)=3.98µs  p(99.9)=25.71µs
     http_req_connecting............: avg=302ns    min=0s      med=0s      max=3.71ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.98ms  min=8.81ms  med=17.12ms max=281.88ms p(90)=23.28ms p(95)=26.05ms p(99.9)=46.27ms
       { expected_response:true }...: avg=17.98ms  min=8.81ms  med=17.12ms max=281.88ms p(90)=23.28ms p(95)=26.05ms p(99.9)=46.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 329885
     http_req_receiving.............: avg=691.83µs min=48.46µs med=81.15µs max=143.69ms p(90)=2.2ms   p(95)=3.62ms  p(99.9)=24.34ms
     http_req_sending...............: avg=42.35µs  min=4.38µs  med=7.4µs   max=165.02ms p(90)=15.89µs p(95)=82.33µs p(99.9)=4.27ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.24ms  min=8.66ms  med=16.42ms max=281.58ms p(90)=22.16ms p(95)=24.85ms p(99.9)=44.29ms
     http_reqs......................: 329885  2725.999577/s
     iteration_duration.............: avg=18.18ms  min=9.06ms  med=17.31ms max=301.22ms p(90)=23.48ms p(95)=26.28ms p(99.9)=46.61ms
     iterations.....................: 329785  2725.173229/s
     success_rate...................: 100.00% ✓ 329785      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 900603      ✗ 0     
     data_received..................: 26 GB   217 MB/s
     data_sent......................: 361 MB  3.0 MB/s
     http_req_blocked...............: avg=2.59µs   min=802ns   med=1.79µs  max=10.79ms  p(90)=3.21µs   p(95)=4.03µs  p(99.9)=25.57µs
     http_req_connecting............: avg=306ns    min=0s      med=0s      max=4.05ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.77ms  min=12.24ms med=19.02ms max=287.77ms p(90)=24.09ms  p(95)=26.19ms p(99.9)=46.14ms
       { expected_response:true }...: avg=19.77ms  min=12.24ms med=19.02ms max=287.77ms p(90)=24.09ms  p(95)=26.19ms p(99.9)=46.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 300301
     http_req_receiving.............: avg=350.51µs min=47.71µs med=80.19µs max=87.83ms  p(90)=865.26µs p(95)=1.84ms  p(99.9)=11.99ms
     http_req_sending...............: avg=39.88µs  min=3.9µs   med=7.5µs   max=199.7ms  p(90)=16.4µs   p(95)=79.12µs p(99.9)=3.1ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.38ms  min=11.92ms med=18.65ms max=287.12ms p(90)=23.53ms  p(95)=25.59ms p(99.9)=44.86ms
     http_reqs......................: 300301  2472.59239/s
     iteration_duration.............: avg=19.97ms  min=12.42ms med=19.21ms max=305.43ms p(90)=24.28ms  p(95)=26.39ms p(99.9)=46.47ms
     iterations.....................: 300201  2471.769019/s
     success_rate...................: 100.00% ✓ 300201      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 899301      ✗ 0     
     data_received..................: 26 GB   216 MB/s
     data_sent......................: 360 MB  3.0 MB/s
     http_req_blocked...............: avg=3.21µs  min=912ns   med=2.47µs  max=3.82ms   p(90)=4.17µs  p(95)=5.08µs  p(99.9)=36.2µs 
     http_req_connecting............: avg=335ns   min=0s      med=0s      max=3.78ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.79ms min=12.17ms med=19.08ms max=294.59ms p(90)=23.68ms p(95)=25.91ms p(99.9)=45.46ms
       { expected_response:true }...: avg=19.79ms min=12.17ms med=19.08ms max=294.59ms p(90)=23.68ms p(95)=25.91ms p(99.9)=45.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 299867
     http_req_receiving.............: avg=86.58µs min=24.56µs med=49.25µs max=209.01ms p(90)=97.97µs p(95)=163.8µs p(99.9)=4.33ms 
     http_req_sending...............: avg=43.74µs min=4.65µs  med=9.42µs  max=172.23ms p(90)=18.6µs  p(95)=95.84µs p(99.9)=2.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.66ms min=12.1ms  med=18.97ms max=294.31ms p(90)=23.53ms p(95)=25.7ms  p(99.9)=44.73ms
     http_reqs......................: 299867  2469.953266/s
     iteration_duration.............: avg=20ms    min=12.34ms med=19.28ms max=304.58ms p(90)=23.89ms p(95)=26.15ms p(99.9)=45.92ms
     iterations.....................: 299767  2469.129583/s
     success_rate...................: 100.00% ✓ 299767      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 888645      ✗ 0     
     data_received..................: 26 GB   214 MB/s
     data_sent......................: 356 MB  2.9 MB/s
     http_req_blocked...............: avg=2.6µs    min=802ns   med=1.83µs  max=10.26ms  p(90)=3.23µs  p(95)=4.06µs  p(99.9)=24.59µs
     http_req_connecting............: avg=321ns    min=0s      med=0s      max=3.63ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20.04ms  min=12.79ms med=19.27ms max=289.86ms p(90)=24.25ms p(95)=26.42ms p(99.9)=46.49ms
       { expected_response:true }...: avg=20.04ms  min=12.79ms med=19.27ms max=289.86ms p(90)=24.25ms p(95)=26.42ms p(99.9)=46.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 296315
     http_req_receiving.............: avg=392.28µs min=50.39µs med=82.86µs max=171.44ms p(90)=1.06ms  p(95)=1.97ms  p(99.9)=14.48ms
     http_req_sending...............: avg=38.22µs  min=4.48µs  med=7.76µs  max=169.63ms p(90)=17.43µs p(95)=82.78µs p(99.9)=3.19ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.61ms  min=12.66ms med=18.88ms max=289.31ms p(90)=23.65ms p(95)=25.74ms p(99.9)=44.96ms
     http_reqs......................: 296315  2439.378528/s
     iteration_duration.............: avg=20.24ms  min=13.02ms med=19.46ms max=298.3ms  p(90)=24.45ms p(95)=26.63ms p(99.9)=46.88ms
     iterations.....................: 296215  2438.55529/s
     success_rate...................: 100.00% ✓ 296215      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 888414      ✗ 0     
     data_received..................: 26 GB   214 MB/s
     data_sent......................: 356 MB  2.9 MB/s
     http_req_blocked...............: avg=2.6µs    min=812ns   med=1.82µs  max=10.39ms  p(90)=3.29µs  p(95)=4.12µs  p(99.9)=29.19µs
     http_req_connecting............: avg=333ns    min=0s      med=0s      max=4.34ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20.04ms  min=12.68ms med=19.27ms max=303.32ms p(90)=24.47ms p(95)=26.6ms  p(99.9)=47.1ms 
       { expected_response:true }...: avg=20.04ms  min=12.68ms med=19.27ms max=303.32ms p(90)=24.47ms p(95)=26.6ms  p(99.9)=47.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 296238
     http_req_receiving.............: avg=423.51µs min=51.26µs med=83.37µs max=217.38ms p(90)=1.22ms  p(95)=2.12ms  p(99.9)=14.87ms
     http_req_sending...............: avg=40.19µs  min=4.3µs   med=7.63µs  max=128.31ms p(90)=16.86µs p(95)=81.51µs p(99.9)=3.71ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.58ms  min=12.59ms med=18.83ms max=302.65ms p(90)=23.86ms p(95)=25.95ms p(99.9)=45.4ms 
     http_reqs......................: 296238  2438.669953/s
     iteration_duration.............: avg=20.25ms  min=12.87ms med=19.47ms max=312.25ms p(90)=24.67ms p(95)=26.81ms p(99.9)=47.48ms
     iterations.....................: 296138  2437.84674/s
     success_rate...................: 100.00% ✓ 296138      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 697674      ✗ 0     
     data_received..................: 20 GB   167 MB/s
     data_sent......................: 280 MB  2.3 MB/s
     http_req_blocked...............: avg=3.54µs   min=831ns   med=1.97µs  max=12.06ms  p(90)=3.74µs  p(95)=4.54µs  p(99.9)=30.97µs
     http_req_connecting............: avg=1.02µs   min=0s      med=0s      max=9.13ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.57ms  min=17.39ms med=25ms    max=299.45ms p(90)=29.71ms p(95)=31.51ms p(99.9)=48.78ms
       { expected_response:true }...: avg=25.57ms  min=17.39ms med=25ms    max=299.45ms p(90)=29.71ms p(95)=31.51ms p(99.9)=48.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 232658
     http_req_receiving.............: avg=481.01µs min=48.83µs med=92.31µs max=151.16ms p(90)=1.43ms  p(95)=2.21ms  p(99.9)=12.94ms
     http_req_sending...............: avg=34.7µs   min=4.53µs  med=8.36µs  max=242.85ms p(90)=18.74µs p(95)=41.69µs p(99.9)=2.13ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.05ms  min=17.26ms med=24.53ms max=293.62ms p(90)=28.93ms p(95)=30.64ms p(99.9)=47.16ms
     http_reqs......................: 232658  1908.320717/s
     iteration_duration.............: avg=25.79ms  min=17.6ms  med=25.21ms max=308.79ms p(90)=29.91ms p(95)=31.71ms p(99.9)=49.06ms
     iterations.....................: 232558  1907.500491/s
     success_rate...................: 100.00% ✓ 232558      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-10 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 691056      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 277 MB  2.3 MB/s
     http_req_blocked...............: avg=3.99µs   min=1µs     med=2.5µs    max=9.53ms   p(90)=4.16µs  p(95)=4.93µs  p(99.9)=34.27µs
     http_req_connecting............: avg=1.03µs   min=0s      med=0s       max=8.96ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.81ms  min=17.33ms med=25.19ms  max=303.81ms p(90)=30.28ms p(95)=32.23ms p(99.9)=50.68ms
       { expected_response:true }...: avg=25.81ms  min=17.33ms med=25.19ms  max=303.81ms p(90)=30.28ms p(95)=32.23ms p(99.9)=50.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 230452
     http_req_receiving.............: avg=470.38µs min=50.04µs med=108.69µs max=180.62ms p(90)=1.29ms  p(95)=1.92ms  p(99.9)=9.85ms 
     http_req_sending...............: avg=38.06µs  min=4.69µs  med=9.33µs   max=256.53ms p(90)=18.37µs p(95)=46.66µs p(99.9)=2.59ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.3ms   min=17.22ms med=24.71ms  max=299.88ms p(90)=29.61ms p(95)=31.48ms p(99.9)=48.72ms
     http_reqs......................: 230452  1889.978933/s
     iteration_duration.............: avg=26.03ms  min=17.5ms  med=25.4ms   max=316.61ms p(90)=30.49ms p(95)=32.44ms p(99.9)=51.12ms
     iterations.....................: 230352  1889.158814/s
     success_rate...................: 100.00% ✓ 230352      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 678792      ✗ 0     
     data_received..................: 20 GB   162 MB/s
     data_sent......................: 272 MB  2.2 MB/s
     http_req_blocked...............: avg=3.37µs  min=1.04µs  med=2.73µs  max=5.79ms   p(90)=4.39µs   p(95)=5.17µs   p(99.9)=37.43µs
     http_req_connecting............: avg=209ns   min=0s      med=0s      max=2.35ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.28ms min=17.63ms med=25.8ms  max=297.98ms p(90)=30.06ms  p(95)=31.55ms  p(99.9)=49.69ms
       { expected_response:true }...: avg=26.28ms min=17.63ms med=25.8ms  max=297.98ms p(90)=30.06ms  p(95)=31.55ms  p(99.9)=49.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 226364
     http_req_receiving.............: avg=82.88µs min=26.74µs med=55.13µs max=191.4ms  p(90)=100.78µs p(95)=131.23µs p(99.9)=2.49ms 
     http_req_sending...............: avg=34.9µs  min=4.83µs  med=10.96µs max=112.5ms  p(90)=19.41µs  p(95)=29.2µs   p(99.9)=1.6ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.16ms min=17.52ms med=25.7ms  max=297.27ms p(90)=29.94ms  p(95)=31.41ms  p(99.9)=48.61ms
     http_reqs......................: 226364  1856.295044/s
     iteration_duration.............: avg=26.5ms  min=17.83ms med=26.01ms max=306.42ms p(90)=30.27ms  p(95)=31.76ms  p(99.9)=50ms   
     iterations.....................: 226264  1855.474995/s
     success_rate...................: 100.00% ✓ 226264      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 671136      ✗ 0     
     data_received..................: 20 GB   161 MB/s
     data_sent......................: 269 MB  2.2 MB/s
     http_req_blocked...............: avg=2.84µs   min=851ns   med=1.91µs   max=12.13ms  p(90)=3.53µs  p(95)=4.24µs  p(99.9)=25.91µs
     http_req_connecting............: avg=432ns    min=0s      med=0s       max=3.64ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.59ms  min=17.38ms med=26.01ms  max=294.86ms p(90)=30.89ms p(95)=32.78ms p(99.9)=51.75ms
       { expected_response:true }...: avg=26.59ms  min=17.38ms med=26.01ms  max=294.86ms p(90)=30.89ms p(95)=32.78ms p(99.9)=51.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 223812
     http_req_receiving.............: avg=554.09µs min=49.75µs med=101.59µs max=237.46ms p(90)=1.61ms  p(95)=2.34ms  p(99.9)=12.83ms
     http_req_sending...............: avg=34.86µs  min=4.51µs  med=8.21µs   max=165.29ms p(90)=17.87µs p(95)=36.86µs p(99.9)=2.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26ms     min=17.28ms med=25.47ms  max=294.27ms p(90)=30.05ms p(95)=31.85ms p(99.9)=48.88ms
     http_reqs......................: 223812  1835.85853/s
     iteration_duration.............: avg=26.81ms  min=17.64ms med=26.21ms  max=314.2ms  p(90)=31.09ms p(95)=32.98ms p(99.9)=52.25ms
     iterations.....................: 223712  1835.038262/s
     success_rate...................: 100.00% ✓ 223712      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-10 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 668139      ✗ 0     
     data_received..................: 20 GB   160 MB/s
     data_sent......................: 268 MB  2.2 MB/s
     http_req_blocked...............: avg=2.87µs   min=811ns   med=1.94µs  max=3.77ms   p(90)=3.76µs  p(95)=4.51µs  p(99.9)=29.19µs
     http_req_connecting............: avg=446ns    min=0s      med=0s      max=3.73ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.71ms  min=17.52ms med=26.14ms max=309.06ms p(90)=31.23ms p(95)=33.07ms p(99.9)=51.27ms
       { expected_response:true }...: avg=26.71ms  min=17.52ms med=26.14ms max=309.06ms p(90)=31.23ms p(95)=33.07ms p(99.9)=51.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 222813
     http_req_receiving.............: avg=439.83µs min=50.64µs med=103.1µs max=68.72ms  p(90)=1.22ms  p(95)=1.81ms  p(99.9)=10.73ms
     http_req_sending...............: avg=34.43µs  min=4.5µs   med=8.19µs  max=133.64ms p(90)=18.35µs p(95)=55.63µs p(99.9)=1.91ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26.24ms  min=17.36ms med=25.69ms max=308.85ms p(90)=30.61ms p(95)=32.36ms p(99.9)=49.44ms
     http_reqs......................: 222813  1826.979485/s
     iteration_duration.............: avg=26.93ms  min=17.69ms med=26.35ms max=318.08ms p(90)=31.43ms p(95)=33.27ms p(99.9)=51.79ms
     iterations.....................: 222713  1826.159525/s
     success_rate...................: 100.00% ✓ 222713      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 667059      ✗ 0     
     data_received..................: 20 GB   160 MB/s
     data_sent......................: 267 MB  2.2 MB/s
     http_req_blocked...............: avg=2.94µs   min=801ns   med=2µs     max=4.28ms   p(90)=3.86µs  p(95)=4.63µs  p(99.9)=33.13µs
     http_req_connecting............: avg=472ns    min=0s      med=0s      max=4.24ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.75ms  min=17.83ms med=26.19ms max=304.57ms p(90)=31.07ms p(95)=32.88ms p(99.9)=50.73ms
       { expected_response:true }...: avg=26.75ms  min=17.83ms med=26.19ms max=304.57ms p(90)=31.07ms p(95)=32.88ms p(99.9)=50.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 222453
     http_req_receiving.............: avg=477.84µs min=49.96µs med=96.46µs max=168.77ms p(90)=1.42ms  p(95)=2.18ms  p(99.9)=10.87ms
     http_req_sending...............: avg=33.86µs  min=4.43µs  med=8.44µs  max=161.59ms p(90)=19.16µs p(95)=36.8µs  p(99.9)=1.92ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26.24ms  min=17.64ms med=25.71ms max=304.38ms p(90)=30.34ms p(95)=32.04ms p(99.9)=49.38ms
     http_reqs......................: 222453  1823.910491/s
     iteration_duration.............: avg=26.97ms  min=18.19ms med=26.4ms  max=319.25ms p(90)=31.27ms p(95)=33.08ms p(99.9)=51.28ms
     iterations.....................: 222353  1823.090583/s
     success_rate...................: 100.00% ✓ 222353      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 642267      ✗ 0     
     data_received..................: 19 GB   154 MB/s
     data_sent......................: 257 MB  2.1 MB/s
     http_req_blocked...............: avg=3.54µs   min=891ns   med=2µs     max=8.33ms   p(90)=3.71µs p(95)=4.48µs  p(99.9)=31.58µs
     http_req_connecting............: avg=1.06µs   min=0s      med=0s      max=8.31ms   p(90)=0s     p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=27.79ms  min=17.67ms med=27.3ms  max=291.92ms p(90)=31.9ms p(95)=33.66ms p(99.9)=51.9ms 
       { expected_response:true }...: avg=27.79ms  min=17.67ms med=27.3ms  max=291.92ms p(90)=31.9ms p(95)=33.66ms p(99.9)=51.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 214189
     http_req_receiving.............: avg=616.45µs min=51.98µs med=121.2µs max=124.33ms p(90)=1.7ms  p(95)=2.36ms  p(99.9)=12.79ms
     http_req_sending...............: avg=34.98µs  min=4.63µs  med=8.44µs  max=244.6ms  p(90)=18.3µs p(95)=37.04µs p(99.9)=2.12ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s     p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=27.14ms  min=17.51ms med=26.68ms max=290.93ms p(90)=31ms   p(95)=32.68ms p(99.9)=49.42ms
     http_reqs......................: 214189  1756.423633/s
     iteration_duration.............: avg=28.01ms  min=17.95ms med=27.51ms max=306.86ms p(90)=32.1ms p(95)=33.87ms p(99.9)=52.28ms
     iterations.....................: 214089  1755.603599/s
     success_rate...................: 100.00% ✓ 214089      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: grafbase (HotChocolate subgraphs) (0.53.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 482916      ✗ 0     
     data_received..................: 14 GB   116 MB/s
     data_sent......................: 194 MB  1.6 MB/s
     http_req_blocked...............: avg=4.33µs  min=842ns   med=2.19µs  max=9.36ms   p(90)=4.71µs   p(95)=5.75µs  p(99.9)=39µs   
     http_req_connecting............: avg=1.51µs  min=0s      med=0s      max=9.17ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=37.01ms min=18.15ms med=36.76ms max=309.75ms p(90)=43.59ms  p(95)=45.52ms p(99.9)=60.09ms
       { expected_response:true }...: avg=37.01ms min=18.15ms med=36.76ms max=309.75ms p(90)=43.59ms  p(95)=45.52ms p(99.9)=60.09ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 161072
     http_req_receiving.............: avg=82.14µs min=27.02µs med=53.82µs max=43.69ms  p(90)=121.23µs p(95)=164.7µs p(99.9)=2.19ms 
     http_req_sending...............: avg=32µs    min=4.65µs  med=9.15µs  max=109.37ms p(90)=23.46µs  p(95)=42.03µs p(99.9)=1.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=36.89ms min=18ms    med=36.65ms max=309.3ms  p(90)=43.47ms  p(95)=45.4ms  p(99.9)=59.22ms
     http_reqs......................: 161072  1320.485745/s
     iteration_duration.............: avg=37.26ms min=21.53ms med=36.99ms max=319.91ms p(90)=43.81ms  p(95)=45.74ms p(99.9)=60.4ms 
     iterations.....................: 160972  1319.665934/s
     success_rate...................: 100.00% ✓ 160972      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.361.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 476547      ✗ 0     
     data_received..................: 14 GB   114 MB/s
     data_sent......................: 191 MB  1.6 MB/s
     http_req_blocked...............: avg=3.9µs   min=1.08µs  med=2.91µs  max=4.51ms   p(90)=4.62µs   p(95)=5.42µs   p(99.9)=40.92µs
     http_req_connecting............: avg=644ns   min=0s      med=0s      max=4.46ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=37.52ms min=18.87ms med=36.91ms max=309.07ms p(90)=45.09ms  p(95)=47.71ms  p(99.9)=61.98ms
       { expected_response:true }...: avg=37.52ms min=18.87ms med=36.91ms max=309.07ms p(90)=45.09ms  p(95)=47.71ms  p(99.9)=61.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 158949
     http_req_receiving.............: avg=82.95µs min=27.11µs med=65.3µs  max=32.04ms  p(90)=110.57µs p(95)=134.44µs p(99.9)=1.14ms 
     http_req_sending...............: avg=31.23µs min=5.34µs  med=12.28µs max=169.4ms  p(90)=19.6µs   p(95)=24.77µs  p(99.9)=1.27ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=37.41ms min=18.74ms med=36.8ms  max=308.9ms  p(90)=44.97ms  p(95)=47.58ms  p(99.9)=61.48ms
     http_reqs......................: 158949  1302.388843/s
     iteration_duration.............: avg=37.76ms min=21.45ms med=37.13ms max=323.56ms p(90)=45.3ms   p(95)=47.92ms  p(99.9)=62.32ms
     iterations.....................: 158849  1301.569467/s
     success_rate...................: 100.00% ✓ 158849      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 468744      ✗ 0     
     data_received..................: 14 GB   112 MB/s
     data_sent......................: 188 MB  1.5 MB/s
     http_req_blocked...............: avg=3.3µs   min=901ns   med=2.35µs  max=3.69ms   p(90)=4.05µs  p(95)=4.82µs   p(99.9)=33.61µs 
     http_req_connecting............: avg=597ns   min=0s      med=0s      max=3.65ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=38.16ms min=19.07ms med=37.54ms max=291.15ms p(90)=45.52ms p(95)=48.2ms   p(99.9)=64.84ms 
       { expected_response:true }...: avg=38.16ms min=19.07ms med=37.54ms max=291.15ms p(90)=45.52ms p(95)=48.2ms   p(99.9)=64.84ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 156348
     http_req_receiving.............: avg=76.83µs min=28.3µs  med=60.71µs max=132.69ms p(90)=99.02µs p(95)=117.16µs p(99.9)=1.18ms  
     http_req_sending...............: avg=24.79µs min=4.87µs  med=11µs    max=169.47ms p(90)=18.28µs p(95)=22.23µs  p(99.9)=968.07µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=38.06ms min=18.91ms med=37.44ms max=290.55ms p(90)=45.42ms p(95)=48.09ms  p(99.9)=64.38ms 
     http_reqs......................: 156348  1280.893069/s
     iteration_duration.............: avg=38.39ms min=21.83ms med=37.75ms max=310.54ms p(90)=45.74ms p(95)=48.41ms  p(99.9)=65.27ms 
     iterations.....................: 156248  1280.073811/s
     success_rate...................: 100.00% ✓ 156248      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 185277     ✗ 0    
     data_received..................: 5.4 GB  44 MB/s
     data_sent......................: 74 MB   607 kB/s
     http_req_blocked...............: avg=4.83µs  min=1µs     med=2.99µs  max=3.52ms   p(90)=4.53µs   p(95)=5.18µs   p(99.9)=48.64µs 
     http_req_connecting............: avg=1.61µs  min=0s      med=0s      max=3.5ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=96.79ms min=21.71ms med=97.88ms max=325.26ms p(90)=139.55ms p(95)=152.91ms p(99.9)=251.99ms
       { expected_response:true }...: avg=96.79ms min=21.71ms med=97.88ms max=325.26ms p(90)=139.55ms p(95)=152.91ms p(99.9)=251.99ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 61859
     http_req_receiving.............: avg=88.77µs min=29.56µs med=77.96µs max=107.2ms  p(90)=112.25µs p(95)=125.37µs p(99.9)=629.57µs
     http_req_sending...............: avg=20.44µs min=4.87µs  med=14.55µs max=93.89ms  p(90)=20.48µs  p(95)=22.62µs  p(99.9)=583.52µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.68ms min=21.61ms med=97.79ms max=324.49ms p(90)=139.44ms p(95)=152.82ms p(99.9)=251.3ms 
     http_reqs......................: 61859   505.71328/s
     iteration_duration.............: avg=97.17ms min=31.37ms med=98.17ms max=332.86ms p(90)=139.81ms p(95)=153.25ms p(99.9)=254.74ms
     iterations.....................: 61759   504.895754/s
     success_rate...................: 100.00% ✓ 61759      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.18.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 145584     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 58 MB   477 kB/s
     http_req_blocked...............: avg=5.41µs   min=1.1µs   med=3.17µs   max=4.23ms   p(90)=4.69µs   p(95)=5.25µs   p(99.9)=615µs   
     http_req_connecting............: avg=2.02µs   min=0s      med=0s       max=4.19ms   p(90)=0s       p(95)=0s       p(99.9)=588.18µs
     http_req_duration..............: avg=123.2ms  min=21.13ms med=121.09ms max=335.74ms p(90)=154.42ms p(95)=164.56ms p(99.9)=210.6ms 
       { expected_response:true }...: avg=123.2ms  min=21.13ms med=121.09ms max=335.74ms p(90)=154.42ms p(95)=164.56ms p(99.9)=210.6ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 48628
     http_req_receiving.............: avg=89.35µs  min=27.58µs med=81.34µs  max=123.23ms p(90)=112.99µs p(95)=125.23µs p(99.9)=533.18µs
     http_req_sending...............: avg=36.23µs  min=5.1µs   med=15.86µs  max=200.41ms p(90)=21.06µs  p(95)=22.99µs  p(99.9)=517µs   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.07ms min=20.98ms med=120.98ms max=335.48ms p(90)=154.31ms p(95)=164.45ms p(99.9)=209.27ms
     http_reqs......................: 48628   397.407073/s
     iteration_duration.............: avg=123.68ms min=43.45ms med=121.4ms  max=354.66ms p(90)=154.75ms p(95)=164.86ms p(99.9)=211.97ms
     iterations.....................: 48528   396.589834/s
     success_rate...................: 100.00% ✓ 48528      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-v3 (HotChocolate subgraphs) (v3.0.0-preview.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 135132     ✗ 0    
     data_received..................: 3.9 GB  32 MB/s
     data_sent......................: 54 MB   443 kB/s
     http_req_blocked...............: avg=5.78µs   min=1.24µs  med=3.73µs   max=3.98ms   p(90)=5.28µs   p(95)=5.86µs   p(99.9)=288.39µs
     http_req_connecting............: avg=1.82µs   min=0s      med=0s       max=3.94ms   p(90)=0s       p(95)=0s       p(99.9)=264.46µs
     http_req_duration..............: avg=132.71ms min=21.64ms med=130.89ms max=349.77ms p(90)=164.87ms p(95)=175.58ms p(99.9)=226.15ms
       { expected_response:true }...: avg=132.71ms min=21.64ms med=130.89ms max=349.77ms p(90)=164.87ms p(95)=175.58ms p(99.9)=226.15ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 45144
     http_req_receiving.............: avg=95.67µs  min=30.12µs med=84.52µs  max=176.44ms p(90)=116.92µs p(95)=129.04µs p(99.9)=510.46µs
     http_req_sending...............: avg=27.79µs  min=5.86µs  med=16.6µs   max=119.38ms p(90)=22.15µs  p(95)=24.1µs   p(99.9)=535.52µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=132.59ms min=21.49ms med=130.77ms max=342.26ms p(90)=164.75ms p(95)=175.46ms p(99.9)=225.45ms
     http_reqs......................: 45144   368.84766/s
     iteration_duration.............: avg=133.24ms min=36.98ms med=131.2ms  max=357.57ms p(90)=165.17ms p(95)=175.92ms p(99.9)=230.11ms
     iterations.....................: 45044   368.030613/s
     success_rate...................: 100.00% ✓ 45044      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-gateway (HotChocolate subgraphs) (2.14.4)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 96270      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   315 kB/s
     http_req_blocked...............: avg=6.05µs   min=1.14µs  med=3.14µs   max=4.63ms   p(90)=4.58µs   p(95)=5.15µs   p(99.9)=1.04ms  
     http_req_connecting............: avg=2.49µs   min=0s      med=0s       max=4.1ms    p(90)=0s       p(95)=0s       p(99.9)=895.66µs
     http_req_duration..............: avg=186.26ms min=23.66ms med=184.99ms max=400.76ms p(90)=196.95ms p(95)=201.62ms p(99.9)=268.24ms
       { expected_response:true }...: avg=186.26ms min=23.66ms med=184.99ms max=400.76ms p(90)=196.95ms p(95)=201.62ms p(99.9)=268.24ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32190
     http_req_receiving.............: avg=92.8µs   min=31.62µs med=87.3µs   max=79.5ms   p(90)=118.2µs  p(95)=129.71µs p(99.9)=380.04µs
     http_req_sending...............: avg=30.39µs  min=5.11µs  med=16.65µs  max=182.56ms p(90)=21.4µs   p(95)=23.23µs  p(99.9)=488.92µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.14ms min=23.52ms med=184.88ms max=400.59ms p(90)=196.84ms p(95)=201.49ms p(99.9)=267.84ms
     http_reqs......................: 32190   262.418573/s
     iteration_duration.............: avg=187.07ms min=62.57ms med=185.3ms  max=406.92ms p(90)=197.23ms p(95)=201.92ms p(99.9)=272.39ms
     iterations.....................: 32090   261.603355/s
     success_rate...................: 100.00% ✓ 32090      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 95004      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   313 kB/s
     http_req_blocked...............: avg=7.27µs   min=1.43µs  med=4.02µs   max=4.44ms   p(90)=5.73µs   p(95)=6.41µs   p(99.9)=1.39ms  
     http_req_connecting............: avg=2.96µs   min=0s      med=0s       max=4.4ms    p(90)=0s       p(95)=0s       p(99.9)=1.37ms  
     http_req_duration..............: avg=188.72ms min=18.1ms  med=173.84ms max=787.53ms p(90)=221.28ms p(95)=240.26ms p(99.9)=718.29ms
       { expected_response:true }...: avg=188.72ms min=18.1ms  med=173.84ms max=787.53ms p(90)=221.28ms p(95)=240.26ms p(99.9)=718.29ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31768
     http_req_receiving.............: avg=100.27µs min=37.33µs med=95.07µs  max=19.8ms   p(90)=127.24µs p(95)=141.15µs p(99.9)=698.06µs
     http_req_sending...............: avg=32.24µs  min=7.29µs  med=19.13µs  max=122.92ms p(90)=24.34µs  p(95)=26.37µs  p(99.9)=663.29µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=188.59ms min=17.77ms med=173.69ms max=787.45ms p(90)=221.15ms p(95)=240.18ms p(99.9)=718.18ms
     http_reqs......................: 31768   260.294926/s
     iteration_duration.............: avg=189.57ms min=43.82ms med=174.29ms max=787.73ms p(90)=221.64ms p(95)=240.83ms p(99.9)=718.58ms
     iterations.....................: 31668   259.475564/s
     success_rate...................: 100.00% ✓ 31668      ✗ 0    
     vus............................: 27      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

