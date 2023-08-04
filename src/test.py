import requests

data = {
        "__EVENTTARGET" : "btnSearch",
        "__EVENTARGUMENT" : "",
        "__VIEWSTATE" : "JGUtwGNOa%2BWwcU4zk5laXn4QNk8YlyltItUzmKpkBKF1%2BJF2KZgjFxRCIhNKTToJI6dGpiEkWd4rgxQOJX3vaVJurerXR1uWR5wR9znCtmKm155ZaXuQt%2B0dXMFI2GyzmNyj6Yt8YnVhmjhbKigxNrPBKdpQCB6AZMaOKreJLAr6EobS9LXPsJ%2BUjV0TgdapQdqdZMsvtO%2FMdaLem7hULmjKcRwwG8uSiEWLvYLYZoQE%2FuSdK8BxpSourz7ZPT7cSTqiSjM%2BU2VMmQl9mBy4IsDNRiVv8xNV0kbGOmE1kzZYLLjqZnmcoMNMn3x1CVROoTugLvJgH4xY0S1BRXeVc%2FfwjMuc7vImfBsZ2Qe2ooFofNkvzjz2L%2Boc796aCW%2BPtZT4F5hapQwKHOq%2BoeTnvU8vfgxjiof4xhl%2BFCo6G5to%2BEq1xu44IWIEJgjBrytjuW8SlA0hMyx%2F2hsVnh0drCOqG%2FAJIoBkOfs0zjB46DUORzRhSyughBW7Kv8DtTm0SotDeaID8rF9nhpDui9zlIJXIY0ZXjvVaNfiHCG2Sh%2B8xzd%2Fkic3EYZo%2FvSsV53j250F%2FDp40RRteWl0%2F9YndlcMOi9h3umpGTroTejU8hhtbtX4ZUbsaP1dcIDLEMV9BSvs1vCSHG%2BHYT6KdIzEwjl%2F87%2BHzOfu6Z%2BFadMsyF2AFS0IT6KjJc0pnmBPUXbB7W%2B%2F3c0nfbHcrgqnGasvBGtdCJFEajAy87lKWB4aiSsMQd7xE8EQZ63fHbeXLceQG45TgvEjGE2oMnaFf3vcrYw6y1khz5JoMczjUh1RfPCXHoJ3a%2BPgdiBoIGhS8Hg81mE6QalFctLd5P8r6FkxhEPyynT5%2BEmHtls4TVAKPqHTSuxWEQro1Ng3kMKCshwZ09cE7%2F3pyitcMhnRjK0U%2BNs7i8beFSsHeGyKGOOWa8v8M9x8Ex%2FmRf9jwCeu4wAuEwCI9gh7nw3Unq687tLECyS1fAGPV28CATR1YqYtKwlk6OjtRqah0w%2FjsO3rSI15GyZiIrVKJNEnxDhiIrBH6sq5xMldHzbOMWurEtUzZzG4j6kyg6ir9GNrDqNFTf27HJPEeTw%2BdUskcPl%2FLEN1ORB%2B666chLwYKQi5zXgeuM3BrWti72CQEtXUXMvk6TOCIVRQnPVh0HH6mxzBdVdGJOWRsIuPzsw0%2F2YAqYMjATkuKvYgxXCBc5zLspTigLjoltJuR4CI5D9pypkaPOFNnE2d0ks%3D",
        "__VIEWSTATEGENERATOR" : "F1918523",
        "__VIEWSTATEENCRYPTED" : "",
        "__EVENTVALIDATION" : "0M%2FmqG%2Fu60b9hokSSRN3tJpboKw58rxy%2Bj%2F0Dq%2BibC3Y0fFM%2FPP7pibvx8B92XZxlath4yWyD4RucLeOXk3TgZrRy1MGa4mmarMzqgDpkP1Y9W6l1GOt4k%2B6UI4lQ9bl4FNzZUIqLBfI1uxGIFQQV%2FL5s1iWL6Q7TrpdNFVrOpB5RHjZoUr5t42iMqJWr0bRRpzbP6xNbtbEiX5QyE3TY5uwKtTURZjlV8W3GdSe4Sim%2BfdZDWy%2B7a343IXjE1ahfJxKeIARGcLb8lZLUoN0W2TAFQ7KzU1SPFTUQCMjLdUXKYpF865InpitN%2BHIKuV66DHNd%2FHOkGD2jvS4xYvOtpsAqwYtT%2BE%2B8nYK7nnWcnwSyRyxuerAXKa7m1HSioScmnLv5Y6EznvjM0HnVuHiWKZfF4mbIyKWAM%2BGKmg1d14N8BlI%2BIGP2uz2OljHEtBl3FWNwpV7sRocv%2F8Oa04Ylk31hFK6%2BW6%2F8X1r4VoZLJgwx7ICwo3CuaCGmlmylOxJDPOWxMVShZ1c4Ms1dDAjLSc2v2vrFfLHw2FO9CNAyAPFsaV0JZ5teqpIFJXqpdIVjhoBcR%2FP047mbR%2BXjThqUXsFFUOHkZYl3Atq8F5I4oGwFqvAjIDgSeLbj1vKCXTQsoOMkTeXr0IpnCArtZFgd3mcrdGFFbIoi4eJuoyjGs5iXmAufU31E%2BvxSDIShJvbB2L%2BqyTyqNCYtFGGsejq6gSrdLornAjcyGLQXdytvMiBUV%2BoSiIHk10lSDUX0oo%2FxYx9ZmxyhejaaSV09TT9xCraf8HJpI035DnsQj1BHfRspxJfGwNNxfuGNIS1SHC5a7kghABU0foyXrO4wOyC2u4mP9etXN%2FPWvdkLkrejh%2FdVRCWSgvkIyIBwSOGqzFIuzyXzb%2Bfg4bvcOalj5jzZRnPPggk%2Fqhy0gnuZMQYhKuDDLkunIYqgFw0yKvDFDPWLaswmoPbCR0WAJMADs6RblUqYaA5rcyBeFIcrtDAA1xS25AxWjpyCVLRyn2D1AOyNtJSSRDKhZs2B03%2F8fc27WWb9hfjAQY0FLZrJ926sSchQ3nY",
        "txtEmail" : "",
        "txtPSWD" : "",
        "txtSrchAuthor" : "",
        "txtSrchCountry" : "United+States",
        "txtSrchTitle" : "",
        "txtSrchReason" : "",
        "txtSrchSubject" : "",
        "txtSrchType" : "",
        "txtSrchJournal" : "",
        "txtSrchPublisher" : "",
        "txtSrchInstitution" : "",
        "txtSrchNotes" : "",
        "txtSrchAdminNotes" : "",
        "txtSrchURL" : "",
        "txtOriginalDateFrom" : "",
        "txtOriginalDateTo" : "",
        "txtOriginalPubMedID" : "",
        "txtOriginalDOI" : "",
        "txtFromDate" : "",
        "txtToDate" : "",
        "txtPubMedID" : "",
        "txtDOI" : "",
        "drpNature" : "",
        "drpSrchPaywalled" : "",
        "txtCreateFromDate" : "",
        "txtCreateToDate" : "",
        "drpSrchApproved" : "",
        "hidClearSearch" : "Y",
        "hidSqlParmNames" : "",
        "hidEmptySqlParmNames" : ""
        }

url  = "http://retractiondatabase.org/RetractionSearch.aspx"
response = requests.post(url=url, data=data)
print(response.text)