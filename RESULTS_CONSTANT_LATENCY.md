## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-net-11 | 16.7.0 | 2,760 | 2,854 | 2,744 | 1.4% |  |
| fusion-aot-11 | 16.7.0 | 2,693 | 2,802 | 2,671 | 1.6% |  |
| feddi-gateway | 3c75a7db8876 | 2,483 | 2,580 | 2,467 | 1.5% |  |
| fusion-fed-net-11 | 16.7.0 | 2,446 | 2,528 | 2,432 | 1.3% |  |
| fusion-fed-aot-11 | 16.7.0 | 2,426 | 2,514 | 2,420 | 1.3% |  |
| hive-router | v0.3.5 | 1,900 | 1,946 | 1,885 | 1.1% |  |
| caliban | 3.2.0 | 1,422 | 1,480 | 1,417 | 1.7% |  |
| cosmo | 0.361.0 | 1,369 | 1,414 | 1,360 | 1.3% |  |
| grafbase | 0.53.5 | 1,323 | 1,348 | 1,315 | 0.8% |  |
| hive-gateway-router-runtime | 2.15.2 | 493 | 510 | 492 | 1.4% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 397 | 415 | 396 | 1.7% |  |
| apollo-router | v2.18.0 | 395 | 416 | 392 | 2.1% |  |
| apollo-gateway | 2.14.4 | 256 | 262 | 255 | 0.8% |  |
| hive-gateway | 2.15.2 | 248 | 255 | 246 | 1.2% |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1001700     ✗ 0     
     data_received..................: 29 GB   242 MB/s
     data_sent......................: 401 MB  3.3 MB/s
     http_req_blocked...............: avg=2.57µs   min=781ns  med=1.8µs   max=17.54ms  p(90)=3.04µs  p(95)=3.86µs  p(99.9)=26.2µs 
     http_req_connecting............: avg=296ns    min=0s     med=0s      max=3.9ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.75ms  min=8.62ms med=16.96ms max=285.86ms p(90)=22.89ms p(95)=25.4ms  p(99.9)=45.72ms
       { expected_response:true }...: avg=17.75ms  min=8.62ms med=16.96ms max=285.86ms p(90)=22.89ms p(95)=25.4ms  p(99.9)=45.72ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 334000
     http_req_receiving.............: avg=729.55µs min=49.8µs med=84.13µs max=146.11ms p(90)=2.42ms  p(95)=3.83ms  p(99.9)=20.39ms
     http_req_sending...............: avg=44.37µs  min=4.34µs med=7.64µs  max=198.19ms p(90)=16.33µs p(95)=86.26µs p(99.9)=4.87ms 
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=16.98ms  min=8.53ms med=16.22ms max=261.67ms p(90)=21.73ms p(95)=24.2ms  p(99.9)=44.01ms
     http_reqs......................: 334000  2760.395849/s
     iteration_duration.............: avg=17.96ms  min=8.82ms med=17.15ms max=297.68ms p(90)=23.09ms p(95)=25.62ms p(99.9)=46.13ms
     iterations.....................: 333900  2759.569383/s
     success_rate...................: 100.00% ✓ 333900      ✗ 0     
     vus............................: 26      min=26        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 977580      ✗ 0     
     data_received..................: 29 GB   236 MB/s
     data_sent......................: 392 MB  3.2 MB/s
     http_req_blocked...............: avg=3.03µs   min=902ns  med=2.2µs   max=13.08ms  p(90)=3.52µs  p(95)=4.21µs  p(99.9)=29.9µs 
     http_req_connecting............: avg=286ns    min=0s     med=0s      max=3.92ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=18.19ms  min=8.51ms med=17.27ms max=287.92ms p(90)=23.72ms p(95)=26.7ms  p(99.9)=48ms   
       { expected_response:true }...: avg=18.19ms  min=8.51ms med=17.27ms max=287.92ms p(90)=23.72ms p(95)=26.7ms  p(99.9)=48ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 325960
     http_req_receiving.............: avg=713.66µs min=50.8µs med=84.85µs max=177.7ms  p(90)=2.26ms  p(95)=3.72ms  p(99.9)=24.28ms
     http_req_sending...............: avg=43.02µs  min=4.63µs med=8.22µs  max=137.76ms p(90)=16.01µs p(95)=87.88µs p(99.9)=4.32ms 
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.43ms  min=8.4ms  med=16.56ms max=287.53ms p(90)=22.56ms p(95)=25.44ms p(99.9)=45.8ms 
     http_reqs......................: 325960  2693.894508/s
     iteration_duration.............: avg=18.4ms   min=8.74ms med=17.46ms max=306.23ms p(90)=23.92ms p(95)=26.92ms p(99.9)=48.58ms
     iterations.....................: 325860  2693.068059/s
     success_rate...................: 100.00% ✓ 325860      ✗ 0     
     vus............................: 40      min=40        max=50  
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

     checks.........................: 100.00% ✓ 904095      ✗ 0     
     data_received..................: 26 GB   217 MB/s
     data_sent......................: 362 MB  3.0 MB/s
     http_req_blocked...............: avg=3µs     min=912ns   med=2.13µs  max=9.55ms   p(90)=3.95µs  p(95)=5µs      p(99.9)=34.77µs
     http_req_connecting............: avg=342ns   min=0s      med=0s      max=3.77ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.68ms min=12.3ms  med=18.97ms max=304.33ms p(90)=23.48ms p(95)=25.72ms  p(99.9)=45.41ms
       { expected_response:true }...: avg=19.68ms min=12.3ms  med=18.97ms max=304.33ms p(90)=23.48ms p(95)=25.72ms  p(99.9)=45.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 301465
     http_req_receiving.............: avg=84.42µs min=24.04µs med=45.81µs max=202.9ms  p(90)=96.92µs p(95)=153.18µs p(99.9)=4.51ms 
     http_req_sending...............: avg=44.15µs min=4.66µs  med=8.97µs  max=185.42ms p(90)=19.76µs p(95)=89.71µs  p(99.9)=3.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.55ms min=12.24ms med=18.87ms max=304.11ms p(90)=23.33ms p(95)=25.49ms  p(99.9)=44.69ms
     http_reqs......................: 301465  2483.165094/s
     iteration_duration.............: avg=19.9ms  min=12.54ms med=19.17ms max=314.77ms p(90)=23.68ms p(95)=25.94ms  p(99.9)=45.8ms 
     iterations.....................: 301365  2482.341395/s
     success_rate...................: 100.00% ✓ 301365      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 891090      ✗ 0     
     data_received..................: 26 GB   214 MB/s
     data_sent......................: 357 MB  2.9 MB/s
     http_req_blocked...............: avg=3.15µs  min=812ns   med=1.83µs  max=11.42ms  p(90)=3.28µs  p(95)=4.09µs  p(99.9)=26.16µs
     http_req_connecting............: avg=805ns   min=0s      med=0s      max=8.98ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.98ms min=12.64ms med=19.25ms max=293.15ms p(90)=24.2ms  p(95)=26.29ms p(99.9)=46.23ms
       { expected_response:true }...: avg=19.98ms min=12.64ms med=19.25ms max=293.15ms p(90)=24.2ms  p(95)=26.29ms p(99.9)=46.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 297130
     http_req_receiving.............: avg=383.7µs min=50.21µs med=82.77µs max=77.01ms  p(90)=1.03ms  p(95)=1.97ms  p(99.9)=13.56ms
     http_req_sending...............: avg=38.91µs min=4.23µs  med=7.71µs  max=193.49ms p(90)=16.75µs p(95)=81.87µs p(99.9)=3.1ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.56ms min=12.52ms med=18.86ms max=292.67ms p(90)=23.61ms p(95)=25.67ms p(99.9)=44.64ms
     http_reqs......................: 297130  2446.069321/s
     iteration_duration.............: avg=20.19ms min=12.84ms med=19.45ms max=306.35ms p(90)=24.39ms p(95)=26.5ms  p(99.9)=46.62ms
     iterations.....................: 297030  2445.246089/s
     success_rate...................: 100.00% ✓ 297030      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 883791      ✗ 0     
     data_received..................: 26 GB   213 MB/s
     data_sent......................: 354 MB  2.9 MB/s
     http_req_blocked...............: avg=3.67µs   min=1.02µs  med=2.33µs  max=16.81ms  p(90)=3.87µs  p(95)=4.66µs  p(99.9)=33.16µs
     http_req_connecting............: avg=751ns    min=0s      med=0s      max=8.35ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20.14ms  min=12.47ms med=19.33ms max=292.66ms p(90)=24.5ms  p(95)=26.86ms p(99.9)=47.18ms
       { expected_response:true }...: avg=20.14ms  min=12.47ms med=19.33ms max=292.66ms p(90)=24.5ms  p(95)=26.86ms p(99.9)=47.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 294697
     http_req_receiving.............: avg=385.77µs min=50.06µs med=84.61µs max=182.8ms  p(90)=980.5µs p(95)=1.98ms  p(99.9)=15.15ms
     http_req_sending...............: avg=40.55µs  min=4.65µs  med=8.59µs  max=184.53ms p(90)=17.51µs p(95)=90.2µs  p(99.9)=3.31ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.71ms  min=12.39ms med=18.94ms max=286.18ms p(90)=23.91ms p(95)=26.22ms p(99.9)=45.74ms
     http_reqs......................: 294697  2426.346123/s
     iteration_duration.............: avg=20.35ms  min=12.66ms med=19.53ms max=303.71ms p(90)=24.71ms p(95)=27.08ms p(99.9)=47.53ms
     iterations.....................: 294597  2425.522787/s
     success_rate...................: 100.00% ✓ 294597      ✗ 0     
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

     checks.........................: 100.00% ✓ 694791      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 278 MB  2.3 MB/s
     http_req_blocked...............: avg=3.63µs  min=1.06µs  med=2.71µs  max=7.48ms   p(90)=4.5µs    p(95)=5.33µs   p(99.9)=40.22µs
     http_req_connecting............: avg=395ns   min=0s      med=0s      max=3.68ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=25.67ms min=17.6ms  med=25.15ms max=302.95ms p(90)=29.35ms  p(95)=30.87ms  p(99.9)=48.49ms
       { expected_response:true }...: avg=25.67ms min=17.6ms  med=25.15ms max=302.95ms p(90)=29.35ms  p(95)=30.87ms  p(99.9)=48.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 231697
     http_req_receiving.............: avg=84.09µs min=25.31µs med=54.8µs  max=166.51ms p(90)=102.54µs p(95)=135.08µs p(99.9)=2.86ms 
     http_req_sending...............: avg=36.51µs min=4.93µs  med=10.68µs max=150.65ms p(90)=19.85µs  p(95)=32.18µs  p(99.9)=1.7ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=25.55ms min=17.52ms med=25.05ms max=302.33ms p(90)=29.22ms  p(95)=30.72ms  p(99.9)=47.51ms
     http_reqs......................: 231697  1900.465297/s
     iteration_duration.............: avg=25.89ms min=17.99ms med=25.37ms max=329.18ms p(90)=29.57ms  p(95)=31.08ms  p(99.9)=48.89ms
     iterations.....................: 231597  1899.64506/s
     success_rate...................: 100.00% ✓ 231597      ✗ 0     
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

     checks.........................: 100.00% ✓ 520470      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=3.79µs  min=952ns   med=2.74µs  max=4.66ms   p(90)=5µs      p(95)=5.91µs   p(99.9)=43.75µs
     http_req_connecting............: avg=573ns   min=0s      med=0s      max=4.13ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.33ms min=18.81ms med=33.81ms max=301.88ms p(90)=40ms     p(95)=42.15ms  p(99.9)=57.56ms
       { expected_response:true }...: avg=34.33ms min=18.81ms med=33.81ms max=301.88ms p(90)=40ms     p(95)=42.15ms  p(99.9)=57.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 173590
     http_req_receiving.............: avg=86.74µs min=27.56µs med=64.09µs max=110.17ms p(90)=112.55µs p(95)=138.98µs p(99.9)=1.98ms 
     http_req_sending...............: avg=31.54µs min=5.02µs  med=12.13µs max=167.38ms p(90)=22.24µs  p(95)=27.59µs  p(99.9)=1.32ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.21ms min=18.61ms med=33.7ms  max=301.68ms p(90)=39.88ms  p(95)=42ms     p(99.9)=56.62ms
     http_reqs......................: 173590  1422.499254/s
     iteration_duration.............: avg=34.57ms min=21.69ms med=34.03ms max=310.49ms p(90)=40.22ms  p(95)=42.37ms  p(99.9)=57.87ms
     iterations.....................: 173490  1421.679795/s
     success_rate...................: 100.00% ✓ 173490      ✗ 0     
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

     checks.........................: 100.00% ✓ 500994      ✗ 0     
     data_received..................: 15 GB   120 MB/s
     data_sent......................: 201 MB  1.6 MB/s
     http_req_blocked...............: avg=3.97µs  min=1.18µs  med=2.96µs  max=4.09ms   p(90)=4.77µs   p(95)=5.59µs   p(99.9)=42.13µs
     http_req_connecting............: avg=616ns   min=0s      med=0s      max=4.04ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=35.68ms min=18.93ms med=35.05ms max=315.38ms p(90)=42.74ms  p(95)=45.25ms  p(99.9)=59.08ms
       { expected_response:true }...: avg=35.68ms min=18.93ms med=35.05ms max=315.38ms p(90)=42.74ms  p(95)=45.25ms  p(99.9)=59.08ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 167098
     http_req_receiving.............: avg=82.71µs min=25.02µs med=62.86µs max=220.81ms p(90)=106.98µs p(95)=130.29µs p(99.9)=1.3ms  
     http_req_sending...............: avg=30.4µs  min=5.04µs  med=11.92µs max=143.19ms p(90)=19.86µs  p(95)=25.39µs  p(99.9)=1.19ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=35.57ms min=18.78ms med=34.95ms max=313.88ms p(90)=42.63ms  p(95)=45.12ms  p(99.9)=58.55ms
     http_reqs......................: 167098  1369.315567/s
     iteration_duration.............: avg=35.92ms min=20.3ms  med=35.27ms max=327.07ms p(90)=42.96ms  p(95)=45.46ms  p(99.9)=59.34ms
     iterations.....................: 166998  1368.496099/s
     success_rate...................: 100.00% ✓ 166998      ✗ 0     
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

     checks.........................: 100.00% ✓ 483912      ✗ 0     
     data_received..................: 14 GB   116 MB/s
     data_sent......................: 194 MB  1.6 MB/s
     http_req_blocked...............: avg=3.37µs  min=821ns   med=2.18µs  max=4.2ms    p(90)=4.73µs   p(95)=5.74µs   p(99.9)=41.49µs
     http_req_connecting............: avg=563ns   min=0s      med=0s      max=4.07ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.94ms min=18.38ms med=36.65ms max=300.53ms p(90)=43.59ms  p(95)=45.53ms  p(99.9)=62.35ms
       { expected_response:true }...: avg=36.94ms min=18.38ms med=36.65ms max=300.53ms p(90)=43.59ms  p(95)=45.53ms  p(99.9)=62.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 161404
     http_req_receiving.............: avg=85.19µs min=26.08µs med=53.78µs max=135.87ms p(90)=122.13µs p(95)=168.07µs p(99.9)=2.19ms 
     http_req_sending...............: avg=34.61µs min=4.33µs  med=9.05µs  max=87.86ms  p(90)=23.99µs  p(95)=64.68µs  p(99.9)=1.94ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=36.82ms min=18.15ms med=36.54ms max=300.18ms p(90)=43.47ms  p(95)=45.41ms  p(99.9)=61.41ms
     http_reqs......................: 161404  1323.113912/s
     iteration_duration.............: avg=37.18ms min=20.41ms med=36.88ms max=323.91ms p(90)=43.8ms   p(95)=45.75ms  p(99.9)=63.02ms
     iterations.....................: 161304  1322.294159/s
     success_rate...................: 100.00% ✓ 161304      ✗ 0     
     vus............................: 4       min=0         max=50  
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

     checks.........................: 100.00% ✓ 180621     ✗ 0    
     data_received..................: 5.3 GB  43 MB/s
     data_sent......................: 72 MB   592 kB/s
     http_req_blocked...............: avg=7.44µs  min=1.32µs  med=3.46µs  max=9.06ms   p(90)=5.08µs   p(95)=5.79µs   p(99.9)=52.84µs 
     http_req_connecting............: avg=3.52µs  min=0s      med=0s      max=8.81ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=99.27ms min=20.93ms med=97.63ms max=329.34ms p(90)=117.59ms p(95)=128.43ms p(99.9)=228.53ms
       { expected_response:true }...: avg=99.27ms min=20.93ms med=97.63ms max=329.34ms p(90)=117.59ms p(95)=128.43ms p(99.9)=228.53ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 60307
     http_req_receiving.............: avg=83.36µs min=30.71µs med=76.75µs max=15.17ms  p(90)=110.01µs p(95)=122.52µs p(99.9)=611.98µs
     http_req_sending...............: avg=25.66µs min=5.7µs   med=15.33µs max=91.72ms  p(90)=21.45µs  p(95)=23.74µs  p(99.9)=1ms     
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=99.16ms min=20.78ms med=97.53ms max=327.29ms p(90)=117.49ms p(95)=128.28ms p(99.9)=228.12ms
     http_reqs......................: 60307   493.139771/s
     iteration_duration.............: avg=99.66ms min=47.91ms med=97.9ms  max=353.43ms p(90)=117.84ms p(95)=128.73ms p(99.9)=231.37ms
     iterations.....................: 60207   492.322056/s
     success_rate...................: 100.00% ✓ 60207      ✗ 0    
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

     checks.........................: 100.00% ✓ 145590     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 58 MB   477 kB/s
     http_req_blocked...............: avg=5.69µs   min=1.07µs  med=3.31µs   max=4.41ms   p(90)=4.86µs   p(95)=5.44µs   p(99.9)=495.62µs
     http_req_connecting............: avg=2.15µs   min=0s      med=0s       max=4.37ms   p(90)=0s       p(95)=0s       p(99.9)=474.09µs
     http_req_duration..............: avg=123.17ms min=21.24ms med=121.45ms max=347.4ms  p(90)=152.94ms p(95)=162.84ms p(99.9)=208.47ms
       { expected_response:true }...: avg=123.17ms min=21.24ms med=121.45ms max=347.4ms  p(90)=152.94ms p(95)=162.84ms p(99.9)=208.47ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48630
     http_req_receiving.............: avg=86.03µs  min=29.2µs  med=83.66µs  max=3.05ms   p(90)=114.48µs p(95)=127.15µs p(99.9)=582.65µs
     http_req_sending...............: avg=25.82µs  min=5.12µs  med=16.17µs  max=85.15ms  p(90)=21.63µs  p(95)=23.61µs  p(99.9)=609.91µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.06ms min=21.15ms med=121.34ms max=346.61ms p(90)=152.82ms p(95)=162.72ms p(99.9)=208.37ms
     http_reqs......................: 48630   397.321813/s
     iteration_duration.............: avg=123.67ms min=52.78ms med=121.76ms max=363.49ms p(90)=153.25ms p(95)=163.17ms p(99.9)=211.18ms
     iterations.....................: 48530   396.504782/s
     success_rate...................: 100.00% ✓ 48530      ✗ 0    
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

     checks.........................: 100.00% ✓ 144795     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   475 kB/s
     http_req_blocked...............: avg=5.26µs   min=981ns   med=3.21µs   max=3.53ms   p(90)=4.67µs   p(95)=5.25µs   p(99.9)=147.49µs
     http_req_connecting............: avg=1.84µs   min=0s      med=0s       max=3.48ms   p(90)=0s       p(95)=0s       p(99.9)=68.89µs 
     http_req_duration..............: avg=123.85ms min=20.53ms med=121.89ms max=341.3ms  p(90)=155.14ms p(95)=165.7ms  p(99.9)=212.34ms
       { expected_response:true }...: avg=123.85ms min=20.53ms med=121.89ms max=341.3ms  p(90)=155.14ms p(95)=165.7ms  p(99.9)=212.34ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48365
     http_req_receiving.............: avg=90.84µs  min=27.74µs med=82.32µs  max=117.81ms p(90)=113.05µs p(95)=125.26µs p(99.9)=600.78µs
     http_req_sending...............: avg=20.25µs  min=5.27µs  med=15.71µs  max=38.95ms  p(90)=20.69µs  p(95)=22.52µs  p(99.9)=594.9µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.74ms min=20.43ms med=121.78ms max=340.56ms p(90)=155.04ms p(95)=165.59ms p(99.9)=211.42ms
     http_reqs......................: 48365   395.329226/s
     iteration_duration.............: avg=124.34ms min=39ms    med=122.2ms  max=349.58ms p(90)=155.41ms p(95)=165.99ms p(99.9)=215.68ms
     iterations.....................: 48265   394.511839/s
     success_rate...................: 100.00% ✓ 48265      ✗ 0    
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

     checks.........................: 100.00% ✓ 93969      ✗ 0    
     data_received..................: 2.8 GB  22 MB/s
     data_sent......................: 38 MB   308 kB/s
     http_req_blocked...............: avg=6.28µs   min=1.09µs  med=3.1µs    max=3.97ms   p(90)=4.51µs   p(95)=5.05µs   p(99.9)=1.31ms  
     http_req_connecting............: avg=2.96µs   min=0s      med=0s       max=3.93ms   p(90)=0s       p(95)=0s       p(99.9)=1.29ms  
     http_req_duration..............: avg=190.84ms min=23.34ms med=191.59ms max=362.52ms p(90)=202.76ms p(95)=207.11ms p(99.9)=278.87ms
       { expected_response:true }...: avg=190.84ms min=23.34ms med=191.59ms max=362.52ms p(90)=202.76ms p(95)=207.11ms p(99.9)=278.87ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31423
     http_req_receiving.............: avg=91.75µs  min=29.85µs med=88.34µs  max=21.38ms  p(90)=118.36µs p(95)=130.19µs p(99.9)=538.01µs
     http_req_sending...............: avg=23.57µs  min=5.5µs   med=16.59µs  max=42.97ms  p(90)=21µs     p(95)=22.87µs  p(99.9)=484.44µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=190.72ms min=23.21ms med=191.46ms max=362.19ms p(90)=202.65ms p(95)=207ms    p(99.9)=278.37ms
     http_reqs......................: 31423   256.132528/s
     iteration_duration.............: avg=191.65ms min=67.98ms med=191.96ms max=371.88ms p(90)=203.06ms p(95)=207.4ms  p(99.9)=280.78ms
     iterations.....................: 31323   255.317416/s
     success_rate...................: 100.00% ✓ 31323      ✗ 0    
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

     checks.........................: 100.00% ✓ 90837      ✗ 0    
     data_received..................: 2.7 GB  22 MB/s
     data_sent......................: 37 MB   298 kB/s
     http_req_blocked...............: avg=7.71µs   min=1.51µs  med=3.84µs   max=3.77ms   p(90)=5.4µs    p(95)=6.07µs   p(99.9)=2.04ms  
     http_req_connecting............: avg=3.59µs   min=0s      med=0s       max=3.73ms   p(90)=0s       p(95)=0s       p(99.9)=2.02ms  
     http_req_duration..............: avg=197.37ms min=17.76ms med=182.32ms max=817.77ms p(90)=238.47ms p(95)=264.41ms p(99.9)=747.38ms
       { expected_response:true }...: avg=197.37ms min=17.76ms med=182.32ms max=817.77ms p(90)=238.47ms p(95)=264.41ms p(99.9)=747.38ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 30379
     http_req_receiving.............: avg=99.3µs   min=36.82µs med=91.78µs  max=29.55ms  p(90)=123.36µs p(95)=136.42µs p(99.9)=891.76µs
     http_req_sending...............: avg=22.72µs  min=5.97µs  med=18.35µs  max=15.92ms  p(90)=23.26µs  p(95)=25.38µs  p(99.9)=506.49µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=197.25ms min=17.62ms med=182.19ms max=817.62ms p(90)=238.33ms p(95)=264.27ms p(99.9)=747.27ms
     http_reqs......................: 30379   248.535063/s
     iteration_duration.............: avg=198.26ms min=46.11ms med=182.74ms max=818.06ms p(90)=238.85ms p(95)=264.94ms p(99.9)=747.72ms
     iterations.....................: 30279   247.716948/s
     success_rate...................: 100.00% ✓ 30279      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

