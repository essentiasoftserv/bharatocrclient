# bharatocr-client
[![Build status](https://github.com/essentiasoftserv/bharatocrclient/actions/workflows/main.yml/badge.svg)](https://github.com/essentiasoftserv/bharatocrclient/actions/workflows/main.yml)

bharatocr-client is an opensource python library to access BharatOcrAPIs

The features of this package:
- Its a package that help to access BharatOcrAPIs in simple way.  


#### Installation


```
    pip install bharatocr-client
```


**Register**

In this function, User can register in the application to use the BharatOcrAPIs.

```
    import bharatocrclient 
    status = bharatocrclient.register(email,password,full_name,use_type)
    # use_type -> must be personal, commercial
```


**Login**

In this function, User must be login in the application before use featured function of the application.

```
    import bharatocrclient 
    key, status = bharatocrclient.login(email, password)
```

**Pan Card**

In this function, User pass the generated key after login and Pan Card image path.

```
    import bharatocrclient 
    dict = bharatocrclient.pan(key, image)
```
**Aadhaar Card**

In this function, User pass the generated key after login and Aadhaar Card image path.

```
    import bharatocrclient 
    dict = b.aadhaar(key, front_image, back_image)
```

### Contribute & support
We are so pleased to your help and help you, If you wanna develop bharatocrclient, Congrats or if you have problem, don't worry create an issue here:

```
    https://github.com/essentiasoftserv/bharatocrclient/issues
```

### Pre Commit
Note: Before commit your changes, run pre-commits 

```
    pre-commit run --all
```
