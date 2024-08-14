# import concurrent.futures
# import multiprocessing
# import requests

# def downloadFiles(url,name):
#     print(f"Started Downloading {name}")
#     response=requests.get(url)
#     open(f"Files/file{name}.jpg","wb").write(response.content)
#     print(f"Finished Downloading {name}")


# # if __name__=='__main__':
#     #  url="https://picsum.photo/2000/3000"
# #normal code 
#     #  props=[]
#     #  for i in range(10):
#     #     #downloadFile(url,i)
#     #     p=multiprocessing.Process(target=downloadFiles,args=[url,i])
#     #     p.start()
#     #     props.append(p)

#     #     for p in props:
#     #         p.join()

#     #  using concurrent method 
# url="https://picsum.photo/2000/3000"
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     l1=[url for i in range(10)]
#     l2=[i for i in range(10)]
#     result=executor.map(downloadFiles,l1,l2)
#     for r in result:
#         print(r)


import concurrent.futures
import requests
import os

def downloadFiles(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    if not os.path.exists("Files"):
        os.makedirs("Files")
    with open(f"Files/file{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"
    
    # Using concurrent.futures.ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for _ in range(10)]
        l2 = [i for i in range(10)]
        result = executor.map(downloadFiles, l1, l2)
        for r in result:
            print(r)
