# Urls-Sorter
A python tool for sorting URLs based on responses.

# Usage
4codes.py inputfile

```python
python3 4codes.py urls.txt
```

sorts urls based on response types i.e 2XX, 3XX, 4XX etc and saves the to a folder called codes with corresponding url in the corresponding  

# Why does this tool exist

On 30/12/2022 i had 3000+ urls from a bugbounty target that i needed to visit. This was gonna be time consuming moreso because most of the sites redirected to the main domain. i tried the multiple urls addon from chrome but that crashed even before starting on my potato pc

```
i7 890 4 core 8 threads
16gb ram
No ssd
```

I asked about a tool that could help me out in our whatsapp group of shield cyber security kenya but i didn't get help until someone pointed out to use chatgpt to create a tool.
Another suggested using the Site: https://httpstatus.io but the site couldn't handle all those urls and i needed a one shot request and also i really wanted something i could create and own in my box for quick access.

The progress folder includes all the scripts that i used chatgpt to write, i later updated and adapted them but the didn't work as i needed.
