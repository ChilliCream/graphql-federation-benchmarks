## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,761 | 4,764 | 4,634 | 1.2% | 416 MB | 89.6 KB |  |
| fusion-net-11 | 16.7.3 | 4,617 | 4,747 | 4,610 | 1.3% | 412 MB | 91.5 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,605 | 4,622 | 4,600 | 0.2% | 408 MB | 90.7 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,592 | 4,610 | 4,445 | 1.8% | 435 MB | 97.0 KB |  |
| fusion-aot-11 | 16.7.3 | 4,476 | 4,485 | 4,455 | 0.3% | 172 MB | 39.4 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,404 | 4,416 | 4,382 | 0.3% | 164 MB | 38.0 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,359 | 4,374 | 4,300 | 0.7% | 171 MB | 40.2 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,279 | 4,303 | 4,254 | 0.4% | 182 MB | 43.6 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,039 | 4,074 | 3,972 | 1.0% | 2,290 MB | 580.5 KB |  |
| hive-router | v0.3.10 | 2,609 | 2,615 | 2,596 | 0.3% | 165 MB | 64.8 KB |  |
| caliban | 3.2.0 | 1,360 | 1,362 | 1,358 | 0.1% | 10,824 MB | 8,149.6 KB |  |
| cosmo | 0.365.2 | 1,340 | 1,342 | 1,338 | 0.1% | 553 MB | 422.2 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 503 | 505 | 500 | 0.4% | 3,161 MB | 6,434.7 KB |  |
| hive-gateway | 2.15.6 | 247 | 248 | 244 | 0.7% | 3,856 MB | 15,987.0 KB |  |
| apollo-gateway | 2.14.4 | 242 | 244 | 242 | 0.4% | 2,482 MB | 10,500.8 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (6608 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (3452 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (174468 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 867471      ✗ 0     
     data_received..................: 25 GB   417 MB/s
     data_sent......................: 349 MB  5.7 MB/s
     http_req_blocked...............: avg=63.68µs  min=811ns    med=2.06µs  max=174.52ms p(90)=3.68µs   p(95)=4.83µs   p(99.9)=23.8ms  
     http_req_connecting............: avg=60.07µs  min=0s       med=0s      max=174.39ms p(90)=0s       p(95)=0s       p(99.9)=23.35ms 
     http_req_duration..............: avg=47.56ms  min=753.85µs med=40.2ms  max=287.85ms p(90)=99.92ms  p(95)=123.69ms p(99.9)=185.37ms
       { expected_response:true }...: avg=47.56ms  min=753.85µs med=40.2ms  max=287.85ms p(90)=99.92ms  p(95)=123.69ms p(99.9)=185.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290157
     http_req_receiving.............: avg=381.19µs min=23.46µs  med=51.17µs max=144.3ms  p(90)=206.19µs p(95)=360.26µs p(99.9)=53.39ms 
     http_req_sending...............: avg=151.58µs min=4.04µs   med=8.41µs  max=255.33ms p(90)=16.9µs   p(95)=116.76µs p(99.9)=27.47ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.03ms  min=711.11µs med=39.9ms  max=283.12ms p(90)=98.72ms  p(95)=122.39ms p(99.9)=174.48ms
     http_reqs......................: 290157  4761.73804/s
     iteration_duration.............: avg=49.26ms  min=1.31ms   med=40.89ms max=326.01ms p(90)=104.01ms p(95)=129.16ms p(99.9)=213.34ms
     iterations.....................: 289157  4745.327139/s
     success_rate...................: 100.00% ✓ 289157      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 841401      ✗ 0     
     data_received..................: 25 GB   404 MB/s
     data_sent......................: 338 MB  5.5 MB/s
     http_req_blocked...............: avg=67.62µs  min=911ns    med=2.59µs  max=128.82ms p(90)=4.17µs   p(95)=5.34µs   p(99.9)=24.91ms 
     http_req_connecting............: avg=63.6µs   min=0s       med=0s      max=128.74ms p(90)=0s       p(95)=0s       p(99.9)=24.32ms 
     http_req_duration..............: avg=48.92ms  min=761.95µs med=41.04ms max=321.96ms p(90)=104.15ms p(95)=128.98ms p(99.9)=179.92ms
       { expected_response:true }...: avg=48.92ms  min=761.95µs med=41.04ms max=321.96ms p(90)=104.15ms p(95)=128.98ms p(99.9)=179.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281467
     http_req_receiving.............: avg=336.04µs min=23.44µs  med=52.71µs max=118.45ms p(90)=219.02µs p(95)=377.46µs p(99.9)=44.08ms 
     http_req_sending...............: avg=156.71µs min=4.03µs   med=9.14µs  max=165.29ms p(90)=17.97µs  p(95)=121.99µs p(99.9)=28.56ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.42ms  min=714.79µs med=40.69ms max=313.38ms p(90)=103.02ms p(95)=127.73ms p(99.9)=174.57ms
     http_reqs......................: 281467  4617.823415/s
     iteration_duration.............: avg=50.79ms  min=1.23ms   med=41.88ms max=331.33ms p(90)=108.31ms p(95)=134.68ms p(99.9)=212.11ms
     iterations.....................: 280467  4601.417145/s
     success_rate...................: 100.00% ✓ 280467      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 841476      ✗ 0     
     data_received..................: 25 GB   403 MB/s
     data_sent......................: 338 MB  5.5 MB/s
     http_req_blocked...............: avg=63.65µs  min=782ns    med=2.12µs  max=114.75ms p(90)=3.79µs   p(95)=4.98µs   p(99.9)=24.01ms 
     http_req_connecting............: avg=60.58µs  min=0s       med=0s      max=114.64ms p(90)=0s       p(95)=0s       p(99.9)=23.94ms 
     http_req_duration..............: avg=49.26ms  min=917.73µs med=41.53ms max=268.14ms p(90)=104.03ms p(95)=127.97ms p(99.9)=181.82ms
       { expected_response:true }...: avg=49.26ms  min=917.73µs med=41.53ms max=268.14ms p(90)=104.03ms p(95)=127.97ms p(99.9)=181.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281492
     http_req_receiving.............: avg=326.4µs  min=23.68µs  med=53.01µs max=115.48ms p(90)=207.4µs  p(95)=368.6µs  p(99.9)=44.32ms 
     http_req_sending...............: avg=146.65µs min=4.16µs   med=8.81µs  max=179.22ms p(90)=17.8µs   p(95)=118.77µs p(99.9)=26.79ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.79ms  min=866.63µs med=41.21ms max=267.88ms p(90)=102.84ms p(95)=126.87ms p(99.9)=176.05ms
     http_reqs......................: 281492  4605.471058/s
     iteration_duration.............: avg=50.78ms  min=1.42ms   med=42.29ms max=313.65ms p(90)=107.21ms p(95)=132.07ms p(99.9)=202.64ms
     iterations.....................: 280492  4589.110128/s
     success_rate...................: 100.00% ✓ 280492      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 838908      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=61.37µs  min=791ns    med=2.08µs  max=127.96ms p(90)=3.79µs   p(95)=4.95µs   p(99.9)=22.7ms  
     http_req_connecting............: avg=58.38µs  min=0s       med=0s      max=127.87ms p(90)=0s       p(95)=0s       p(99.9)=22.6ms  
     http_req_duration..............: avg=49.42ms  min=904µs    med=41.7ms  max=307.87ms p(90)=105.05ms p(95)=129.28ms p(99.9)=178.26ms
       { expected_response:true }...: avg=49.42ms  min=904µs    med=41.7ms  max=307.87ms p(90)=105.05ms p(95)=129.28ms p(99.9)=178.26ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280636
     http_req_receiving.............: avg=302µs    min=24.61µs  med=52.36µs max=112.78ms p(90)=212.1µs  p(95)=371.75µs p(99.9)=40.33ms 
     http_req_sending...............: avg=144.04µs min=4.08µs   med=8.56µs  max=162.04ms p(90)=17.87µs  p(95)=120.34µs p(99.9)=26.85ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.97ms  min=856.75µs med=41.4ms  max=307.23ms p(90)=103.95ms p(95)=128.21ms p(99.9)=174.59ms
     http_reqs......................: 280636  4592.21436/s
     iteration_duration.............: avg=50.94ms  min=1.44ms   med=42.49ms max=329.26ms p(90)=108.06ms p(95)=134.35ms p(99.9)=203.81ms
     iterations.....................: 279636  4575.850763/s
     success_rate...................: 100.00% ✓ 279636      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 816618     ✗ 0     
     data_received..................: 24 GB   392 MB/s
     data_sent......................: 328 MB  5.4 MB/s
     http_req_blocked...............: avg=55.62µs  min=901ns    med=2.51µs  max=111.82ms p(90)=4.13µs   p(95)=5.28µs   p(99.9)=18.03ms 
     http_req_connecting............: avg=52.01µs  min=0s       med=0s      max=111.61ms p(90)=0s       p(95)=0s       p(99.9)=17.75ms 
     http_req_duration..............: avg=50.87ms  min=835.62µs med=42.46ms max=288.57ms p(90)=109.08ms p(95)=135ms    p(99.9)=188.91ms
       { expected_response:true }...: avg=50.87ms  min=835.62µs med=42.46ms max=288.57ms p(90)=109.08ms p(95)=135ms    p(99.9)=188.91ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 273206
     http_req_receiving.............: avg=310.49µs min=25.33µs  med=50.32µs max=124.38ms p(90)=229.36µs p(95)=398µs    p(99.9)=39.8ms  
     http_req_sending...............: avg=136.88µs min=4.39µs   med=8.96µs  max=273.43ms p(90)=18.16µs  p(95)=129.73µs p(99.9)=24.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.42ms  min=791.72µs med=42.19ms max=288.23ms p(90)=107.99ms p(95)=134.06ms p(99.9)=181.23ms
     http_reqs......................: 273206  4476.78352/s
     iteration_duration.............: avg=52.33ms  min=1.37ms   med=43.22ms max=320.07ms p(90)=112.11ms p(95)=139.25ms p(99.9)=210.15ms
     iterations.....................: 272206  4460.39741/s
     success_rate...................: 100.00% ✓ 272206     ✗ 0     
     vus............................: 59      min=0        max=498 
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 803466      ✗ 0     
     data_received..................: 24 GB   385 MB/s
     data_sent......................: 323 MB  5.3 MB/s
     http_req_blocked...............: avg=53.73µs  min=902ns    med=2.45µs  max=122.25ms p(90)=4.1µs    p(95)=5.25µs   p(99.9)=16.65ms 
     http_req_connecting............: avg=50.02µs  min=0s       med=0s      max=120.92ms p(90)=0s       p(95)=0s       p(99.9)=15.85ms 
     http_req_duration..............: avg=51.66ms  min=836.24µs med=42.97ms max=285.28ms p(90)=111.59ms p(95)=139.43ms p(99.9)=192.07ms
       { expected_response:true }...: avg=51.66ms  min=836.24µs med=42.97ms max=285.28ms p(90)=111.59ms p(95)=139.43ms p(99.9)=192.07ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 268822
     http_req_receiving.............: avg=289.85µs min=26.04µs  med=51.55µs max=148.9ms  p(90)=231.73µs p(95)=404.49µs p(99.9)=38.06ms 
     http_req_sending...............: avg=135.31µs min=4.03µs   med=8.83µs  max=86.99ms  p(90)=18.58µs  p(95)=133.28µs p(99.9)=23.05ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.23ms  min=797.75µs med=42.67ms max=268.3ms  p(90)=110.56ms p(95)=138.49ms p(99.9)=186.2ms 
     http_reqs......................: 268822  4404.393676/s
     iteration_duration.............: avg=53.19ms  min=1.42ms   med=43.93ms max=358.83ms p(90)=114.39ms p(95)=142.81ms p(99.9)=211.81ms
     iterations.....................: 267822  4388.009623/s
     success_rate...................: 100.00% ✓ 267822      ✗ 0     
     vus............................: 59      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 797217      ✗ 0     
     data_received..................: 23 GB   382 MB/s
     data_sent......................: 321 MB  5.2 MB/s
     http_req_blocked...............: avg=42.86µs  min=801ns    med=2µs     max=99.88ms  p(90)=3.65µs   p(95)=4.84µs   p(99.9)=11.52ms 
     http_req_connecting............: avg=39.73µs  min=0s       med=0s      max=99.63ms  p(90)=0s       p(95)=0s       p(99.9)=11.44ms 
     http_req_duration..............: avg=52.43ms  min=979.99µs med=44.05ms max=296ms    p(90)=112.17ms p(95)=137.99ms p(99.9)=191.93ms
       { expected_response:true }...: avg=52.43ms  min=979.99µs med=44.05ms max=296ms    p(90)=112.17ms p(95)=137.99ms p(99.9)=191.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 266739
     http_req_receiving.............: avg=251.16µs min=25.62µs  med=50.19µs max=106.08ms p(90)=220.67µs p(95)=379.07µs p(99.9)=32.42ms 
     http_req_sending...............: avg=115.41µs min=4.18µs   med=8.4µs   max=195.49ms p(90)=18.28µs  p(95)=124.45µs p(99.9)=20.49ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=52.06ms  min=938.6µs  med=43.8ms  max=288.93ms p(90)=111.35ms p(95)=137.14ms p(99.9)=188.1ms 
     http_reqs......................: 266739  4359.608819/s
     iteration_duration.............: avg=53.61ms  min=1.66ms   med=44.97ms max=327.18ms p(90)=114.58ms p(95)=140.67ms p(99.9)=203.22ms
     iterations.....................: 265739  4343.264719/s
     success_rate...................: 100.00% ✓ 265739      ✗ 0     
     vus............................: 65      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 782574      ✗ 0     
     data_received..................: 23 GB   374 MB/s
     data_sent......................: 315 MB  5.1 MB/s
     http_req_blocked...............: avg=56.18µs  min=932ns    med=2.6µs   max=118.8ms  p(90)=4.32µs   p(95)=5.55µs   p(99.9)=17.74ms 
     http_req_connecting............: avg=51.97µs  min=0s       med=0s      max=118.56ms p(90)=0s       p(95)=0s       p(99.9)=17.58ms 
     http_req_duration..............: avg=52.86ms  min=979.1µs  med=44.18ms max=308.02ms p(90)=113.34ms p(95)=141.84ms p(99.9)=197.49ms
       { expected_response:true }...: avg=52.86ms  min=979.1µs  med=44.18ms max=308.02ms p(90)=113.34ms p(95)=141.84ms p(99.9)=197.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 261858
     http_req_receiving.............: avg=295.48µs min=25.77µs  med=52.76µs max=123.08ms p(90)=231.97µs p(95)=410.86µs p(99.9)=39.24ms 
     http_req_sending...............: avg=141.31µs min=4.11µs   med=9.1µs   max=254.99ms p(90)=19.61µs  p(95)=135.44µs p(99.9)=25.18ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=52.43ms  min=929.53µs med=43.9ms  max=307.64ms p(90)=112.44ms p(95)=140.77ms p(99.9)=193.81ms
     http_reqs......................: 261858  4279.340595/s
     iteration_duration.............: avg=54.6ms   min=1.48ms   med=45.19ms max=394.62ms p(90)=117.16ms p(95)=145.88ms p(99.9)=233ms   
     iterations.....................: 260858  4262.998377/s
     success_rate...................: 100.00% ✓ 260858      ✗ 0     
     vus............................: 65      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-10-25-0247)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 736098      ✗ 0     
     data_received..................: 22 GB   353 MB/s
     data_sent......................: 296 MB  4.9 MB/s
     http_req_blocked...............: avg=40µs     min=812ns    med=2.1µs   max=93.81ms  p(90)=3.7µs    p(95)=4.86µs   p(99.9)=5.44ms  
     http_req_connecting............: avg=36.73µs  min=0s       med=0s      max=93.63ms  p(90)=0s       p(95)=0s       p(99.9)=5.16ms  
     http_req_duration..............: avg=57.03ms  min=737.1µs  med=48.37ms max=344.07ms p(90)=118.69ms p(95)=144.31ms p(99.9)=216.52ms
       { expected_response:true }...: avg=57.03ms  min=737.1µs  med=48.37ms max=344.07ms p(90)=118.69ms p(95)=144.31ms p(99.9)=216.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 246366
     http_req_receiving.............: avg=246.72µs min=26.22µs  med=50.81µs max=75.48ms  p(90)=210.58µs p(95)=363.71µs p(99.9)=34.04ms 
     http_req_sending...............: avg=109.03µs min=4.16µs   med=8.74µs  max=270.24ms p(90)=17.41µs  p(95)=121.47µs p(99.9)=19.63ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=56.68ms  min=679.08µs med=48.14ms max=328.21ms p(90)=117.99ms p(95)=143.43ms p(99.9)=212.55ms
     http_reqs......................: 246366  4039.734142/s
     iteration_duration.............: avg=58.07ms  min=1.37ms   med=49.14ms max=353.58ms p(90)=120.67ms p(95)=146.5ms  p(99.9)=233.01ms
     iterations.....................: 245366  4023.336854/s
     success_rate...................: 100.00% ✓ 245366      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 479394      ✗ 0     
     data_received..................: 14 GB   228 MB/s
     data_sent......................: 193 MB  3.1 MB/s
     http_req_blocked...............: avg=11.05µs  min=832ns   med=2.25µs  max=32.55ms  p(90)=3.78µs   p(95)=4.9µs    p(99.9)=599.33µs
     http_req_connecting............: avg=7.98µs   min=0s      med=0s      max=32.5ms   p(90)=0s       p(95)=0s       p(99.9)=510.32µs
     http_req_duration..............: avg=88.44ms  min=1.33ms  med=83.92ms max=333.84ms p(90)=171.78ms p(95)=186.62ms p(99.9)=226.43ms
       { expected_response:true }...: avg=88.44ms  min=1.33ms  med=83.92ms max=333.84ms p(90)=171.78ms p(95)=186.62ms p(99.9)=226.43ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 160798
     http_req_receiving.............: avg=114.01µs min=27.52µs med=54.97µs max=92.05ms  p(90)=144.08µs p(95)=342µs    p(99.9)=7.54ms  
     http_req_sending...............: avg=58.77µs  min=4.27µs  med=9.73µs  max=83.83ms  p(90)=18.67µs  p(95)=118.35µs p(99.9)=7.42ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=88.27ms  min=1.26ms  med=83.74ms max=318.08ms p(90)=171.58ms p(95)=186.39ms p(99.9)=225.75ms
     http_reqs......................: 160798  2609.983229/s
     iteration_duration.............: avg=89.22ms  min=3.13ms  med=84.83ms max=350.94ms p(90)=172.2ms  p(95)=186.98ms p(99.9)=227.46ms
     iterations.....................: 159798  2593.751788/s
     success_rate...................: 100.00% ✓ 159798      ✗ 0     
     vus............................: 84      min=0         max=492 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 251805     ✗ 0    
     data_received..................: 7.4 GB  119 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=6.27µs   min=962ns  med=2.87µs   max=26.67ms  p(90)=4.63µs   p(95)=5.58µs   p(99.9)=385.73µs
     http_req_connecting............: avg=2.66µs   min=0s     med=0s       max=26.48ms  p(90)=0s       p(95)=0s       p(99.9)=237.93µs
     http_req_duration..............: avg=167.91ms min=2.03ms med=140.21ms max=846.7ms  p(90)=349.05ms p(95)=405.74ms p(99.9)=659.21ms
       { expected_response:true }...: avg=167.91ms min=2.03ms med=140.21ms max=846.7ms  p(90)=349.05ms p(95)=405.74ms p(99.9)=659.21ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 84935
     http_req_receiving.............: avg=78.26µs  min=27µs   med=61.64µs  max=18.72ms  p(90)=99.87µs  p(95)=117.99µs p(99.9)=1.89ms  
     http_req_sending...............: avg=37.61µs  min=4.94µs med=12.62µs  max=208.69ms p(90)=19.25µs  p(95)=23.08µs  p(99.9)=4.07ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.8ms  min=1.95ms med=140.1ms  max=846.62ms p(90)=348.95ms p(95)=405.64ms p(99.9)=659.13ms
     http_reqs......................: 84935   1360.64424/s
     iteration_duration.............: avg=170.18ms min=7.28ms med=142.86ms max=846.9ms  p(90)=350.47ms p(95)=406.85ms p(99.9)=659.59ms
     iterations.....................: 83935   1344.62441/s
     success_rate...................: 100.00% ✓ 83935      ✗ 0    
     vus............................: 75      min=0        max=493
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.365.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 248142      ✗ 0    
     data_received..................: 7.3 GB  117 MB/s
     data_sent......................: 101 MB  1.6 MB/s
     http_req_blocked...............: avg=5.41µs   min=932ns   med=2.27µs   max=20.35ms  p(90)=4.02µs   p(95)=4.92µs   p(99.9)=377.3µs 
     http_req_connecting............: avg=2.54µs   min=0s      med=0s       max=20.3ms   p(90)=0s       p(95)=0s       p(99.9)=318.8µs 
     http_req_duration..............: avg=170.37ms min=2ms     med=169.11ms max=533.92ms p(90)=322.88ms p(95)=346.1ms  p(99.9)=441.82ms
       { expected_response:true }...: avg=170.37ms min=2ms     med=169.11ms max=533.92ms p(90)=322.88ms p(95)=346.1ms  p(99.9)=441.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 83714
     http_req_receiving.............: avg=72.44µs  min=26.57µs med=58.99µs  max=99.1ms   p(90)=96.1µs   p(95)=110.59µs p(99.9)=1.11ms  
     http_req_sending...............: avg=26.79µs  min=4.65µs  med=10.46µs  max=199.96ms p(90)=17.14µs  p(95)=20.51µs  p(99.9)=3.06ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=170.27ms min=1.94ms  med=169.01ms max=533.85ms p(90)=322.8ms  p(95)=345.98ms p(99.9)=441.76ms
     http_reqs......................: 83714   1340.622633/s
     iteration_duration.............: avg=172.65ms min=5.17ms  med=171.74ms max=534.1ms  p(90)=323.68ms p(95)=346.67ms p(99.9)=442.04ms
     iterations.....................: 82714   1324.608315/s
     success_rate...................: 100.00% ✓ 82714       ✗ 0    
     vus............................: 77      min=0         max=493
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 94596      ✗ 0    
     data_received..................: 2.8 GB  44 MB/s
     data_sent......................: 39 MB   605 kB/s
     http_req_blocked...............: avg=7.92µs   min=1.25µs  med=3.35µs   max=11.63ms  p(90)=5.14µs   p(95)=6.16µs   p(99.9)=653.04µs
     http_req_connecting............: avg=3.5µs    min=0s      med=0s       max=11.56ms  p(90)=0s       p(95)=0s       p(99.9)=587.31µs
     http_req_duration..............: avg=441.38ms min=3.73ms  med=406.28ms max=1.71s    p(90)=872.82ms p(95)=950.48ms p(99.9)=1.42s   
       { expected_response:true }...: avg=441.38ms min=3.73ms  med=406.28ms max=1.71s    p(90)=872.82ms p(95)=950.48ms p(99.9)=1.42s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 32532
     http_req_receiving.............: avg=91.94µs  min=30.17µs med=74.98µs  max=136.21ms p(90)=111.94µs p(95)=125.41µs p(99.9)=1.07ms  
     http_req_sending...............: avg=33.03µs  min=5.45µs  med=15.28µs  max=89.72ms  p(90)=21.77µs  p(95)=24.7µs   p(99.9)=2.75ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=441.26ms min=3.67ms  med=406.17ms max=1.71s    p(90)=872.75ms p(95)=950.41ms p(99.9)=1.42s   
     http_reqs......................: 32532   503.649187/s
     iteration_duration.............: avg=455.64ms min=27.17ms med=425.97ms max=1.71s    p(90)=876.59ms p(95)=954.98ms p(99.9)=1.43s   
     iterations.....................: 31532   488.167532/s
     success_rate...................: 100.00% ✓ 31532      ✗ 0    
     vus............................: 83      min=0        max=498
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 46860      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   297 kB/s
     http_req_blocked...............: avg=15.4µs   min=1.12µs  med=3.71µs   max=15.88ms p(90)=5.62µs  p(95)=7.58µs   p(99.9)=2.11ms  
     http_req_connecting............: avg=9.92µs   min=0s      med=0s       max=15.81ms p(90)=0s      p(95)=0s       p(99.9)=2.09ms  
     http_req_duration..............: avg=876.25ms min=5.56ms  med=804.07ms max=4.99s   p(90)=1.74s   p(95)=1.99s    p(99.9)=4.07s   
       { expected_response:true }...: avg=876.25ms min=5.56ms  med=804.07ms max=4.99s   p(90)=1.74s   p(95)=1.99s    p(99.9)=4.07s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16620
     http_req_receiving.............: avg=94.45µs  min=35.13µs med=88.58µs  max=6.06ms  p(90)=124.5µs p(95)=140.59µs p(99.9)=977.88µs
     http_req_sending...............: avg=33.65µs  min=6.02µs  med=17.51µs  max=26.85ms p(90)=23.1µs  p(95)=26.66µs  p(99.9)=5.49ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=876.12ms min=5.49ms  med=803.92ms max=4.99s   p(90)=1.74s   p(95)=1.99s    p(99.9)=4.07s   
     http_reqs......................: 16620   247.362121/s
     iteration_duration.............: avg=932.36ms min=82.75ms med=864.56ms max=4.99s   p(90)=1.77s   p(95)=2.01s    p(99.9)=4.13s   
     iterations.....................: 15620   232.47872/s
     success_rate...................: 100.00% ✓ 15620      ✗ 0    
     vus............................: 66      min=0        max=498
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 46857      ✗ 0    
     data_received..................: 1.5 GB  21 MB/s
     data_sent......................: 20 MB   291 kB/s
     http_req_blocked...............: avg=14.1µs   min=1.17µs  med=3.05µs   max=7.4ms    p(90)=4.8µs   p(95)=6.38µs   p(99.9)=2.3ms   
     http_req_connecting............: avg=9.38µs   min=0s      med=0s       max=7.34ms   p(90)=0s      p(95)=0s       p(99.9)=2.27ms  
     http_req_duration..............: avg=873.8ms  min=7.59ms  med=792.21ms max=2.97s    p(90)=1.78s   p(95)=1.9s     p(99.9)=2.59s   
       { expected_response:true }...: avg=873.8ms  min=7.59ms  med=792.21ms max=2.97s    p(90)=1.78s   p(95)=1.9s     p(99.9)=2.59s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16619
     http_req_receiving.............: avg=95.97µs  min=31.24µs med=86.45µs  max=33.9ms   p(90)=124.4µs p(95)=140.42µs p(99.9)=944.79µs
     http_req_sending...............: avg=37.95µs  min=5.29µs  med=16.28µs  max=118.13ms p(90)=21.43µs p(95)=24.81µs  p(99.9)=3.46ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=873.67ms min=7.51ms  med=792.11ms max=2.97s    p(90)=1.78s   p(95)=1.9s     p(99.9)=2.59s   
     http_reqs......................: 16619   242.688808/s
     iteration_duration.............: avg=929.76ms min=24.44ms med=877.88ms max=2.98s    p(90)=1.79s   p(95)=1.92s    p(99.9)=2.61s   
     iterations.....................: 15619   228.085714/s
     success_rate...................: 100.00% ✓ 15619      ✗ 0    
     vus............................: 80      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

