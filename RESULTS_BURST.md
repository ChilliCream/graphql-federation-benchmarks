## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| nitro-router | 16.8.0-p.23 | 4,799 | 4,887 | 4,768 | 1.0% | 157 MB | 33.5 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.23 | 4,779 | 4,798 | 4,755 | 0.4% | 374 MB | 80.1 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.23 | 4,766 | 4,887 | 4,724 | 1.3% | 125 MB | 26.9 KB |  |
| nitro-router-fed | 16.8.0-p.23 | 4,749 | 4,761 | 4,732 | 0.3% | 155 MB | 33.4 KB |  |
| fusion-net-11 | 16.7.7 | 4,743 | 4,754 | 4,732 | 0.2% | 415 MB | 89.6 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 4,733 | 4,763 | 4,663 | 1.0% | 159 MB | 34.5 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.23 | 4,725 | 4,745 | 4,714 | 0.2% | 376 MB | 81.5 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.23 | 4,709 | 4,742 | 4,676 | 0.6% | 132 MB | 28.7 KB |  |
| fusion-fed-net-11 | 16.7.7 | 4,702 | 4,783 | 4,682 | 0.8% | 402 MB | 87.6 KB |  |
| feddi-gateway | 2026-11-22-1912 | 4,663 | 4,665 | 4,643 | 0.2% | 2,313 MB | 508.0 KB |  |
| fusion-aot-11 | 16.7.7 | 4,583 | 4,593 | 4,577 | 0.1% | 144 MB | 32.2 KB |  |
| hive-router | v0.3.17 | 4,111 | 4,140 | 4,054 | 1.0% | 196 MB | 48.9 KB |  |
| hive-router-nightly | v0.3.21-nightly.46ee6fa7 | 3,901 | 3,932 | 3,885 | 0.5% | 190 MB | 49.8 KB |  |
| caliban | 3.2.1 | 1,522 | 1,525 | 1,519 | 0.2% | 11,703 MB | 7,873.9 KB |  |
| cosmo | 0.373.0 | 1,330 | 1,332 | 1,318 | 0.5% | 602 MB | 463.8 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 551 | 552 | 547 | 0.4% | 3,015 MB | 5,602.7 KB |  |
| hive-gateway | 2.15.10 | 266 | 269 | 265 | 0.6% | 3,613 MB | 13,908.9 KB |  |
| apollo-gateway | 2.14.4 | 241 | 242 | 240 | 0.3% | 2,443 MB | 10,380.1 KB |  |
| apollo-router | v2.19.1 | — | — | — | — | — | — | non-compatible response (4952 across 5/5 runs) |
| apollo-router-nightly | v3.0.0-preview.0-nightly.b135f054 | — | — | — | — | — | — | non-compatible response (4554 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (4634 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (157416 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: nitro-router (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 874161      ✗ 0     
     data_received..................: 26 GB   420 MB/s
     data_sent......................: 351 MB  5.8 MB/s
     http_req_blocked...............: avg=75.72µs  min=872ns    med=2.57µs  max=157.94ms p(90)=4.04µs   p(95)=5.15µs   p(99.9)=29.91ms 
     http_req_connecting............: avg=72.11µs  min=0s       med=0s      max=157.87ms p(90)=0s       p(95)=0s       p(99.9)=29.53ms 
     http_req_duration..............: avg=46.68ms  min=739.81µs med=39.63ms max=296.99ms p(90)=97.14ms  p(95)=120.26ms p(99.9)=177.55ms
       { expected_response:true }...: avg=46.68ms  min=739.81µs med=39.63ms max=296.99ms p(90)=97.14ms  p(95)=120.26ms p(99.9)=177.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 292387
     http_req_receiving.............: avg=356.04µs min=22.1µs   med=53.97µs max=186.86ms p(90)=208.48µs p(95)=355.84µs p(99.9)=48.21ms 
     http_req_sending...............: avg=162.19µs min=3.92µs   med=9.11µs  max=177.2ms  p(90)=16.44µs  p(95)=116.29µs p(99.9)=28.34ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.17ms  min=692.31µs med=39.24ms max=296.79ms p(90)=95.94ms  p(95)=118.84ms p(99.9)=174ms   
     http_reqs......................: 292387  4799.957017/s
     iteration_duration.............: avg=48.88ms  min=1.19ms   med=40.6ms  max=324.28ms p(90)=103.56ms p(95)=128.15ms p(99.9)=200.89ms
     iterations.....................: 291387  4783.540565/s
     success_rate...................: 100.00% ✓ 291387      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 870222      ✗ 0     
     data_received..................: 26 GB   418 MB/s
     data_sent......................: 350 MB  5.7 MB/s
     http_req_blocked...............: avg=76.56µs  min=842ns    med=2.55µs  max=167.16ms p(90)=4.04µs   p(95)=5.19µs   p(99.9)=29.41ms 
     http_req_connecting............: avg=72.39µs  min=0s       med=0s      max=167.1ms  p(90)=0s       p(95)=0s       p(99.9)=29.11ms 
     http_req_duration..............: avg=46.66ms  min=725.21µs med=39.87ms max=311.85ms p(90)=96.51ms  p(95)=119.19ms p(99.9)=178.28ms
       { expected_response:true }...: avg=46.66ms  min=725.21µs med=39.87ms max=311.85ms p(90)=96.51ms  p(95)=119.19ms p(99.9)=178.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 291074
     http_req_receiving.............: avg=384.21µs min=26.09µs  med=54.91µs max=191.36ms p(90)=209.96µs p(95)=357.79µs p(99.9)=48.94ms 
     http_req_sending...............: avg=168.89µs min=3.96µs   med=8.98µs  max=277.44ms p(90)=16.24µs  p(95)=114.62µs p(99.9)=31.95ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.11ms  min=682.37µs med=39.47ms max=311.58ms p(90)=95.17ms  p(95)=117.86ms p(99.9)=171.37ms
     http_reqs......................: 291074  4779.252118/s
     iteration_duration.............: avg=49.1ms   min=1.18ms   med=40.77ms max=371.31ms p(90)=104ms    p(95)=127.95ms p(99.9)=212.86ms
     iterations.....................: 290074  4762.832747/s
     success_rate...................: 100.00% ✓ 290074      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 868035      ✗ 0     
     data_received..................: 25 GB   417 MB/s
     data_sent......................: 349 MB  5.7 MB/s
     http_req_blocked...............: avg=71.72µs  min=842ns    med=2.56µs  max=141.02ms p(90)=4.02µs   p(95)=5.12µs   p(99.9)=27.22ms 
     http_req_connecting............: avg=68.26µs  min=0s       med=0s      max=140.96ms p(90)=0s       p(95)=0s       p(99.9)=26.99ms 
     http_req_duration..............: avg=46.86ms  min=736.46µs med=39.57ms max=288.51ms p(90)=98.37ms  p(95)=122.28ms p(99.9)=183.05ms
       { expected_response:true }...: avg=46.86ms  min=736.46µs med=39.57ms max=288.51ms p(90)=98.37ms  p(95)=122.28ms p(99.9)=183.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290345
     http_req_receiving.............: avg=369.73µs min=25.46µs  med=53.44µs max=161ms    p(90)=206.41µs p(95)=362.05µs p(99.9)=51.1ms  
     http_req_sending...............: avg=165.39µs min=3.78µs   med=8.81µs  max=173.88ms p(90)=16.54µs  p(95)=117.98µs p(99.9)=30.67ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.32ms  min=700.72µs med=39.22ms max=249.45ms p(90)=97.16ms  p(95)=120.93ms p(99.9)=176.06ms
     http_reqs......................: 290345  4766.186463/s
     iteration_duration.............: avg=49.23ms  min=1.05ms   med=40.59ms max=400.58ms p(90)=104.84ms p(95)=130.83ms p(99.9)=211.57ms
     iterations.....................: 289345  4749.770866/s
     success_rate...................: 100.00% ✓ 289345      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: nitro-router-fed (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 865212      ✗ 0     
     data_received..................: 25 GB   416 MB/s
     data_sent......................: 348 MB  5.7 MB/s
     http_req_blocked...............: avg=76.67µs  min=801ns    med=2.56µs  max=167.14ms p(90)=4.07µs   p(95)=5.22µs   p(99.9)=29.95ms 
     http_req_connecting............: avg=72.29µs  min=0s       med=0s      max=147.54ms p(90)=0s       p(95)=0s       p(99.9)=28.99ms 
     http_req_duration..............: avg=47.29ms  min=769.96µs med=39.85ms max=246.1ms  p(90)=99.56ms  p(95)=122.97ms p(99.9)=185.11ms
       { expected_response:true }...: avg=47.29ms  min=769.96µs med=39.85ms max=246.1ms  p(90)=99.56ms  p(95)=122.97ms p(99.9)=185.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 289404
     http_req_receiving.............: avg=410.8µs  min=25.22µs  med=53.64µs max=139.27ms p(90)=218.07µs p(95)=368.73µs p(99.9)=57.82ms 
     http_req_sending...............: avg=161.64µs min=4µs      med=9.02µs  max=158.41ms p(90)=16.83µs  p(95)=117.68µs p(99.9)=29.04ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.72ms  min=729.2µs  med=39.5ms  max=245.96ms p(90)=98.3ms   p(95)=121.54ms p(99.9)=172.45ms
     http_reqs......................: 289404  4749.297554/s
     iteration_duration.............: avg=49.38ms  min=1.2ms    med=40.75ms max=358.73ms p(90)=105.04ms p(95)=130.45ms p(99.9)=209.66ms
     iterations.....................: 288404  4732.886939/s
     success_rate...................: 100.00% ✓ 288404      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 863850      ✗ 0     
     data_received..................: 25 GB   415 MB/s
     data_sent......................: 347 MB  5.7 MB/s
     http_req_blocked...............: avg=78.28µs  min=811ns    med=2.53µs  max=155.18ms p(90)=4.05µs   p(95)=5.2µs    p(99.9)=31.65ms 
     http_req_connecting............: avg=73.98µs  min=0s       med=0s      max=155.1ms  p(90)=0s       p(95)=0s       p(99.9)=31.17ms 
     http_req_duration..............: avg=47.03ms  min=720.5µs  med=39.78ms max=269.15ms p(90)=98.85ms  p(95)=122.48ms p(99.9)=181.92ms
       { expected_response:true }...: avg=47.03ms  min=720.5µs  med=39.78ms max=269.15ms p(90)=98.85ms  p(95)=122.48ms p(99.9)=181.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288950
     http_req_receiving.............: avg=372.25µs min=23.3µs   med=54.01µs max=245.05ms p(90)=210.9µs  p(95)=362.78µs p(99.9)=48.17ms 
     http_req_sending...............: avg=173.55µs min=3.98µs   med=9.05µs  max=137.07ms p(90)=17.03µs  p(95)=116.36µs p(99.9)=31.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.48ms  min=677.19µs med=39.41ms max=261.27ms p(90)=97.6ms   p(95)=121.07ms p(99.9)=177.82ms
     http_reqs......................: 288950  4743.151134/s
     iteration_duration.............: avg=49.47ms  min=1.3ms    med=40.89ms max=333.88ms p(90)=105.36ms p(95)=130.46ms p(99.9)=214.72ms
     iterations.....................: 287950  4726.736006/s
     success_rate...................: 100.00% ✓ 287950      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 862773      ✗ 0     
     data_received..................: 25 GB   414 MB/s
     data_sent......................: 347 MB  5.7 MB/s
     http_req_blocked...............: avg=67.45µs  min=801ns    med=2.18µs  max=140.87ms p(90)=3.83µs   p(95)=5µs      p(99.9)=24.22ms 
     http_req_connecting............: avg=63.83µs  min=0s       med=0s      max=140.76ms p(90)=0s       p(95)=0s       p(99.9)=23.32ms 
     http_req_duration..............: avg=47.62ms  min=787.73µs med=39.76ms max=325.86ms p(90)=101.1ms  p(95)=126.82ms p(99.9)=181.36ms
       { expected_response:true }...: avg=47.62ms  min=787.73µs med=39.76ms max=325.86ms p(90)=101.1ms  p(95)=126.82ms p(99.9)=181.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288591
     http_req_receiving.............: avg=331.3µs  min=22.39µs  med=52.59µs max=123.63ms p(90)=210.08µs p(95)=365.62µs p(99.9)=45.34ms 
     http_req_sending...............: avg=147.58µs min=4.25µs   med=8.73µs  max=206.83ms p(90)=16.67µs  p(95)=116.43µs p(99.9)=26.8ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.14ms  min=743.82µs med=39.43ms max=325.4ms  p(90)=99.93ms  p(95)=125.51ms p(99.9)=177.92ms
     http_reqs......................: 288591  4733.907542/s
     iteration_duration.............: avg=49.53ms  min=1.2ms    med=40.68ms max=351.74ms p(90)=105.82ms p(95)=133.08ms p(99.9)=209.78ms
     iterations.....................: 287591  4717.504024/s
     success_rate...................: 100.00% ✓ 287591      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 860730      ✗ 0     
     data_received..................: 25 GB   414 MB/s
     data_sent......................: 346 MB  5.7 MB/s
     http_req_blocked...............: avg=75.81µs  min=911ns    med=2.59µs  max=201.95ms p(90)=4.1µs    p(95)=5.26µs   p(99.9)=29.08ms 
     http_req_connecting............: avg=72.04µs  min=0s       med=0s      max=140.01ms p(90)=0s       p(95)=0s       p(99.9)=28.54ms 
     http_req_duration..............: avg=47.55ms  min=726.97µs med=40.76ms max=265.76ms p(90)=98.06ms  p(95)=121.45ms p(99.9)=179.68ms
       { expected_response:true }...: avg=47.55ms  min=726.97µs med=40.76ms max=265.76ms p(90)=98.06ms  p(95)=121.45ms p(99.9)=179.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 287910
     http_req_receiving.............: avg=389.13µs min=21.88µs  med=55.45µs max=158.04ms p(90)=209.33µs p(95)=360.95µs p(99.9)=51.75ms 
     http_req_sending...............: avg=164.46µs min=4.11µs   med=9.23µs  max=139.92ms p(90)=16.76µs  p(95)=114.47µs p(99.9)=29.58ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47ms     min=688.35µs med=40.39ms max=265.54ms p(90)=96.59ms  p(95)=120.04ms p(99.9)=173.2ms 
     http_reqs......................: 287910  4725.824281/s
     iteration_duration.............: avg=49.64ms  min=1.18ms   med=41.47ms max=312.9ms  p(90)=103.74ms p(95)=130.07ms p(99.9)=203.35ms
     iterations.....................: 286910  4709.410039/s
     success_rate...................: 100.00% ✓ 286910      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 857640      ✗ 0     
     data_received..................: 25 GB   412 MB/s
     data_sent......................: 345 MB  5.7 MB/s
     http_req_blocked...............: avg=71.84µs  min=831ns    med=2.44µs  max=137.97ms p(90)=4.01µs   p(95)=5.16µs   p(99.9)=27.37ms 
     http_req_connecting............: avg=67.83µs  min=0s       med=0s      max=137.76ms p(90)=0s       p(95)=0s       p(99.9)=26.69ms 
     http_req_duration..............: avg=47.7ms   min=750.92µs med=39.73ms max=261.42ms p(90)=100.52ms p(95)=125.52ms p(99.9)=184.63ms
       { expected_response:true }...: avg=47.7ms   min=750.92µs med=39.73ms max=261.42ms p(90)=100.52ms p(95)=125.52ms p(99.9)=184.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 286880
     http_req_receiving.............: avg=367.55µs min=24.35µs  med=53.69µs max=174.17ms p(90)=211.39µs p(95)=367.77µs p(99.9)=51.7ms  
     http_req_sending...............: avg=161.8µs  min=4.26µs   med=8.93µs  max=213.27ms p(90)=16.67µs  p(95)=118.31µs p(99.9)=29ms    
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.17ms  min=706µs    med=39.39ms max=250.4ms  p(90)=99.26ms  p(95)=124.08ms p(99.9)=178.87ms
     http_reqs......................: 286880  4709.013659/s
     iteration_duration.............: avg=49.82ms  min=1.16ms   med=40.92ms max=379.32ms p(90)=106.05ms p(95)=133.18ms p(99.9)=207.51ms
     iterations.....................: 285880  4692.599082/s
     success_rate...................: 100.00% ✓ 285880      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 856500      ✗ 0     
     data_received..................: 25 GB   412 MB/s
     data_sent......................: 344 MB  5.7 MB/s
     http_req_blocked...............: avg=71.49µs  min=912ns    med=2.64µs  max=150.98ms p(90)=4.19µs   p(95)=5.34µs   p(99.9)=28.18ms 
     http_req_connecting............: avg=67.82µs  min=0s       med=0s      max=150.91ms p(90)=0s       p(95)=0s       p(99.9)=28.09ms 
     http_req_duration..............: avg=47.71ms  min=742.89µs med=39.96ms max=329.89ms p(90)=100.94ms p(95)=124.94ms p(99.9)=184.14ms
       { expected_response:true }...: avg=47.71ms  min=742.89µs med=39.96ms max=329.89ms p(90)=100.94ms p(95)=124.94ms p(99.9)=184.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 286500
     http_req_receiving.............: avg=360.71µs min=23.27µs  med=53.7µs  max=158.97ms p(90)=217.61µs p(95)=373.6µs  p(99.9)=48.37ms 
     http_req_sending...............: avg=167.53µs min=4.03µs   med=9.36µs  max=183.25ms p(90)=17.4µs   p(95)=119.79µs p(99.9)=30.04ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.18ms  min=701.74µs med=39.61ms max=318.32ms p(90)=99.61ms  p(95)=123.57ms p(99.9)=178.53ms
     http_reqs......................: 286500  4702.907334/s
     iteration_duration.............: avg=49.89ms  min=1.24ms   med=40.93ms max=345.27ms p(90)=106.43ms p(95)=133.04ms p(99.9)=208.67ms
     iterations.....................: 285500  4686.4923/s
     success_rate...................: 100.00% ✓ 285500      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-22-1912)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 849762      ✗ 0     
     data_received..................: 25 GB   408 MB/s
     data_sent......................: 342 MB  5.6 MB/s
     http_req_blocked...............: avg=57.9µs   min=791ns    med=2.05µs  max=114.3ms  p(90)=3.66µs   p(95)=4.75µs   p(99.9)=21.37ms 
     http_req_connecting............: avg=54.86µs  min=0s       med=0s      max=114.18ms p(90)=0s       p(95)=0s       p(99.9)=20.93ms 
     http_req_duration..............: avg=48.63ms  min=746.54µs med=40.71ms max=275.34ms p(90)=103.02ms p(95)=130.08ms p(99.9)=196.82ms
       { expected_response:true }...: avg=48.63ms  min=746.54µs med=40.71ms max=275.34ms p(90)=103.02ms p(95)=130.08ms p(99.9)=196.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 284254
     http_req_receiving.............: avg=311.53µs min=23.38µs  med=51.37µs max=120.31ms p(90)=209.37µs p(95)=377.82µs p(99.9)=44.52ms 
     http_req_sending...............: avg=139.64µs min=4.14µs   med=8.67µs  max=226.47ms p(90)=16.76µs  p(95)=119.95µs p(99.9)=25.28ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.18ms  min=701.89µs med=40.43ms max=275.09ms p(90)=101.95ms p(95)=128.86ms p(99.9)=190.72ms
     http_reqs......................: 284254  4663.6732/s
     iteration_duration.............: avg=50.29ms  min=1.25ms   med=41.44ms max=313.61ms p(90)=106.73ms p(95)=135.15ms p(99.9)=221.4ms 
     iterations.....................: 283254  4647.266489/s
     success_rate...................: 100.00% ✓ 283254      ✗ 0     
     vus............................: 55      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 835368      ✗ 0     
     data_received..................: 25 GB   401 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=72.9µs   min=931ns    med=2.59µs  max=277.51ms p(90)=4.22µs   p(95)=5.4µs    p(99.9)=28.38ms 
     http_req_connecting............: avg=68.32µs  min=0s       med=0s      max=277.47ms p(90)=0s       p(95)=0s       p(99.9)=27.64ms 
     http_req_duration..............: avg=49.34ms  min=783.52µs med=41.15ms max=296.39ms p(90)=106ms    p(95)=132.28ms p(99.9)=188.22ms
       { expected_response:true }...: avg=49.34ms  min=783.52µs med=41.15ms max=296.39ms p(90)=106ms    p(95)=132.28ms p(99.9)=188.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279456
     http_req_receiving.............: avg=329.59µs min=22.86µs  med=53.61µs max=167.16ms p(90)=223.04µs p(95)=392.04µs p(99.9)=44.95ms 
     http_req_sending...............: avg=156.02µs min=4.1µs    med=9.12µs  max=106.3ms  p(90)=17.68µs  p(95)=125.18µs p(99.9)=28ms    
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.86ms  min=735.93µs med=40.82ms max=275.11ms p(90)=104.8ms  p(95)=131.11ms p(99.9)=184.04ms
     http_reqs......................: 279456  4583.707935/s
     iteration_duration.............: avg=51.15ms  min=1.16ms   med=42.13ms max=321.42ms p(90)=110.48ms p(95)=138.57ms p(99.9)=206.2ms 
     iterations.....................: 278456  4567.305682/s
     success_rate...................: 100.00% ✓ 278456      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 750600      ✗ 0     
     data_received..................: 22 GB   360 MB/s
     data_sent......................: 302 MB  4.9 MB/s
     http_req_blocked...............: avg=57.07µs  min=801ns    med=2.59µs  max=181.06ms p(90)=4.48µs   p(95)=5.84µs   p(99.9)=18.46ms 
     http_req_connecting............: avg=52.49µs  min=0s       med=0s      max=181.03ms p(90)=0s       p(95)=0s       p(99.9)=17.38ms 
     http_req_duration..............: avg=55.69ms  min=873.88µs med=46.62ms max=285.97ms p(90)=119.33ms p(95)=151.71ms p(99.9)=211.83ms
       { expected_response:true }...: avg=55.69ms  min=873.88µs med=46.62ms max=285.97ms p(90)=119.33ms p(95)=151.71ms p(99.9)=211.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 251200
     http_req_receiving.............: avg=285.84µs min=24.85µs  med=54.88µs max=153ms    p(90)=223.92µs p(95)=394.23µs p(99.9)=38.81ms 
     http_req_sending...............: avg=137.02µs min=4.22µs   med=9.56µs  max=128.58ms p(90)=19.85µs  p(95)=132.04µs p(99.9)=25.19ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=55.27ms  min=836.49µs med=46.34ms max=285.06ms p(90)=118.37ms p(95)=150.69ms p(99.9)=208.01ms
     http_reqs......................: 251200  4111.00224/s
     iteration_duration.............: avg=56.94ms  min=1.56ms   med=47.34ms max=320.28ms p(90)=122.31ms p(95)=155.13ms p(99.9)=227.36ms
     iterations.....................: 250200  4094.636785/s
     success_rate...................: 100.00% ✓ 250200      ✗ 0     
     vus............................: 61      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.21-nightly.46ee6fa7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 711948      ✗ 0     
     data_received..................: 21 GB   341 MB/s
     data_sent......................: 286 MB  4.7 MB/s
     http_req_blocked...............: avg=51.55µs  min=1.03µs   med=2.9µs   max=138.34ms p(90)=4.78µs   p(95)=6.09µs   p(99.9)=12.32ms 
     http_req_connecting............: avg=47.01µs  min=0s       med=0s      max=138.25ms p(90)=0s       p(95)=0s       p(99.9)=11.33ms 
     http_req_duration..............: avg=58.48ms  min=873.06µs med=48.87ms max=298.69ms p(90)=124.59ms p(95)=156.52ms p(99.9)=219.33ms
       { expected_response:true }...: avg=58.48ms  min=873.06µs med=48.87ms max=298.69ms p(90)=124.59ms p(95)=156.52ms p(99.9)=219.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 238316
     http_req_receiving.............: avg=322.37µs min=26.42µs  med=55.65µs max=199.58ms p(90)=219.07µs p(95)=409.8µs  p(99.9)=54.23ms 
     http_req_sending...............: avg=132.52µs min=4.09µs   med=10.13µs max=199.64ms p(90)=20.11µs  p(95)=135.77µs p(99.9)=24.04ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=58.02ms  min=820.35µs med=48.58ms max=298.33ms p(90)=123.5ms  p(95)=155.18ms p(99.9)=213.09ms
     http_reqs......................: 238316  3901.305658/s
     iteration_duration.............: avg=60.03ms  min=1.56ms   med=50.04ms max=330.57ms p(90)=128.02ms p(95)=160.1ms  p(99.9)=245.46ms
     iterations.....................: 237316  3884.935353/s
     success_rate...................: 100.00% ✓ 237316      ✗ 0     
     vus............................: 61      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 282222      ✗ 0    
     data_received..................: 8.3 GB  133 MB/s
     data_sent......................: 114 MB  1.8 MB/s
     http_req_blocked...............: avg=8.21µs   min=1.14µs  med=3.49µs   max=40.34ms  p(90)=5.66µs   p(95)=6.84µs   p(99.9)=370.99µs
     http_req_connecting............: avg=3.91µs   min=0s      med=0s       max=39.4ms   p(90)=0s       p(95)=0s       p(99.9)=286.72µs
     http_req_duration..............: avg=149.91ms min=1.98ms  med=124.48ms max=947.94ms p(90)=312.5ms  p(95)=372.37ms p(99.9)=640.04ms
       { expected_response:true }...: avg=149.91ms min=1.98ms  med=124.48ms max=947.94ms p(90)=312.5ms  p(95)=372.37ms p(99.9)=640.04ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 95074
     http_req_receiving.............: avg=93.85µs  min=28.89µs med=68.73µs  max=29.9ms   p(90)=113.48µs p(95)=143.87µs p(99.9)=2.77ms  
     http_req_sending...............: avg=47.26µs  min=5.14µs  med=14.21µs  max=228.27ms p(90)=22.36µs  p(95)=28.66µs  p(99.9)=5.26ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=149.76ms min=1.92ms  med=124.33ms max=947.85ms p(90)=312.38ms p(95)=372.24ms p(99.9)=639.97ms
     http_reqs......................: 95074   1522.333755/s
     iteration_duration.............: avg=151.77ms min=7.17ms  med=126.52ms max=948.11ms p(90)=313.93ms p(95)=373.68ms p(99.9)=641.14ms
     iterations.....................: 94074   1506.321662/s
     success_rate...................: 100.00% ✓ 94074       ✗ 0    
     vus............................: 78      min=0         max=493
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.373.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 246270      ✗ 0    
     data_received..................: 7.3 GB  116 MB/s
     data_sent......................: 100 MB  1.6 MB/s
     http_req_blocked...............: avg=4.93µs   min=921ns   med=2.22µs   max=20.15ms  p(90)=3.81µs   p(95)=4.75µs   p(99.9)=284.45µs
     http_req_connecting............: avg=2.07µs   min=0s      med=0s       max=20.11ms  p(90)=0s       p(95)=0s       p(99.9)=205.13µs
     http_req_duration..............: avg=171.65ms min=1.99ms  med=171.95ms max=549.13ms p(90)=319.26ms p(95)=342.92ms p(99.9)=465.39ms
       { expected_response:true }...: avg=171.65ms min=1.99ms  med=171.95ms max=549.13ms p(90)=319.26ms p(95)=342.92ms p(99.9)=465.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 83090
     http_req_receiving.............: avg=76.34µs  min=27.39µs med=58.77µs  max=231.86ms p(90)=95.79µs  p(95)=112.31µs p(99.9)=1.23ms  
     http_req_sending...............: avg=26.77µs  min=4.65µs  med=9.95µs   max=94.77ms  p(90)=16.18µs  p(95)=19.85µs  p(99.9)=3.16ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=171.55ms min=1.93ms  med=171.84ms max=549.05ms p(90)=319.17ms p(95)=342.83ms p(99.9)=465.32ms
     http_reqs......................: 83090   1330.798982/s
     iteration_duration.............: avg=173.97ms min=4.56ms  med=174.53ms max=549.35ms p(90)=319.88ms p(95)=343.55ms p(99.9)=465.87ms
     iterations.....................: 82090   1314.782627/s
     success_rate...................: 100.00% ✓ 82090       ✗ 0    
     vus............................: 77      min=0         max=493
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 103077     ✗ 0    
     data_received..................: 3.1 GB  48 MB/s
     data_sent......................: 42 MB   662 kB/s
     http_req_blocked...............: avg=9.13µs   min=1.1µs  med=3.03µs   max=12.96ms p(90)=4.66µs   p(95)=5.63µs   p(99.9)=1.48ms
     http_req_connecting............: avg=5.1µs    min=0s     med=0s       max=12.89ms p(90)=0s       p(95)=0s       p(99.9)=1.45ms
     http_req_duration..............: avg=405.63ms min=3.38ms med=374.92ms max=1.61s   p(90)=806.05ms p(95)=880.37ms p(99.9)=1.28s 
       { expected_response:true }...: avg=405.63ms min=3.38ms med=374.92ms max=1.61s   p(90)=806.05ms p(95)=880.37ms p(99.9)=1.28s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 35359
     http_req_receiving.............: avg=165.84µs min=31.4µs med=70.29µs  max=221.2ms p(90)=106.37µs p(95)=120.04µs p(99.9)=1.94ms
     http_req_sending...............: avg=24.59µs  min=5.29µs med=13.57µs  max=43.55ms p(90)=19.9µs   p(95)=22.54µs  p(99.9)=2.71ms
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=405.44ms min=3.32ms med=374.84ms max=1.61s   p(90)=805.94ms p(95)=880.26ms p(99.9)=1.28s 
     http_reqs......................: 35359   551.580743/s
     iteration_duration.............: avg=417.67ms min=5.35ms med=389.7ms  max=1.61s   p(90)=809.86ms p(95)=884.13ms p(99.9)=1.29s 
     iterations.....................: 34359   535.981298/s
     success_rate...................: 100.00% ✓ 34359      ✗ 0    
     vus............................: 63      min=0        max=497
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 50640      ✗ 0    
     data_received..................: 1.6 GB  23 MB/s
     data_sent......................: 22 MB   320 kB/s
     http_req_blocked...............: avg=14.48µs  min=1.43µs  med=3.53µs   max=14.25ms p(90)=5.28µs   p(95)=6.74µs   p(99.9)=2.19ms 
     http_req_connecting............: avg=9.36µs   min=0s      med=0s       max=14.2ms  p(90)=0s       p(95)=0s       p(99.9)=2.16ms 
     http_req_duration..............: avg=812.25ms min=5.22ms  med=715.18ms max=4.04s   p(90)=1.64s    p(95)=1.9s     p(99.9)=3.47s  
       { expected_response:true }...: avg=812.25ms min=5.22ms  med=715.18ms max=4.04s   p(90)=1.64s    p(95)=1.9s     p(99.9)=3.47s  
     http_req_failed................: 0.00%   ✓ 0          ✗ 17880
     http_req_receiving.............: avg=144.52µs min=39.21µs med=85.37µs  max=77.12ms p(90)=123.09µs p(95)=138.43µs p(99.9)=14.87ms
     http_req_sending...............: avg=29.63µs  min=5.87µs  med=16.19µs  max=15.72ms p(90)=21.89µs  p(95)=25.15µs  p(99.9)=3.35ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=812.08ms min=5.14ms  med=715.09ms max=4.04s   p(90)=1.64s    p(95)=1.9s     p(99.9)=3.47s  
     http_reqs......................: 17880   266.246199/s
     iteration_duration.............: avg=860.42ms min=25.62ms med=790.02ms max=4.05s   p(90)=1.65s    p(95)=1.92s    p(99.9)=3.48s  
     iterations.....................: 16880   251.355472/s
     success_rate...................: 100.00% ✓ 16880      ✗ 0    
     vus............................: 61      min=0        max=499
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

     checks.........................: 100.00% ✓ 46698      ✗ 0    
     data_received..................: 1.5 GB  21 MB/s
     data_sent......................: 20 MB   290 kB/s
     http_req_blocked...............: avg=11.27µs  min=1.1µs   med=3.11µs   max=10.11ms p(90)=4.78µs  p(95)=6.19µs   p(99.9)=1.18ms 
     http_req_connecting............: avg=6.57µs   min=0s      med=0s       max=10.04ms p(90)=0s      p(95)=0s       p(99.9)=1.16ms 
     http_req_duration..............: avg=875.5ms  min=7.57ms  med=795.1ms  max=2.78s   p(90)=1.78s   p(95)=1.92s    p(99.9)=2.53s  
       { expected_response:true }...: avg=875.5ms  min=7.57ms  med=795.1ms  max=2.78s   p(90)=1.78s   p(95)=1.92s    p(99.9)=2.53s  
     http_req_failed................: 0.00%   ✓ 0          ✗ 16566
     http_req_receiving.............: avg=92.92µs  min=31.22µs med=84.31µs  max=39.13ms p(90)=120.9µs p(95)=137.18µs p(99.9)=956.3µs
     http_req_sending...............: avg=32.74µs  min=5.25µs  med=15.86µs  max=48.3ms  p(90)=21.04µs p(95)=24.42µs  p(99.9)=2.74ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=875.38ms min=7.5ms   med=795ms    max=2.78s   p(90)=1.78s   p(95)=1.92s    p(99.9)=2.53s  
     http_reqs......................: 16566   241.676473/s
     iteration_duration.............: avg=931.69ms min=32.9ms  med=897.33ms max=2.78s   p(90)=1.8s    p(95)=1.92s    p(99.9)=2.55s  
     iterations.....................: 15566   227.087769/s
     success_rate...................: 100.00% ✓ 15566      ✗ 0    
     vus............................: 83      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

