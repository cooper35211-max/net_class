
while True:
    try:
        fileName = input("輸入檔案名稱 ==> ")
        inputFile = open(fileName,"r") 
        while True:
            num = inputFile.readline()
            if (num == ""): break
            print("讀入資料的倒數 = ",1/int(num))
    except IOError:
        print("\n*** 輸入資料檔不存在 ***\n")
    except ValueError:
        print("\n*** 偵測到非整數的字符，請輸入整數 ***\n")
    except ZeroDivisionError:
        print("\n*** 發生除0錯誤，輸入不能為0 ***\n")
    except KeyboardInterrupt:
        print("\n\n你按了^C或^Break鍵將迫使程式關閉\n")
        exit(0)
    except:
        print("發生其他異常")
    else:
        print("\n讀檔+資料轉換順利，未發生預期的例外\n")
        inputFile.close()
    #finally:
    #    print("\n已處理一輪，再接再厲\n")



'''
while True:
	fileName = input("輸入檔案名稱 ==> ")
	inputFile = open(fileName,"r") 
	while True:
		num = inputFile.readline()
		if (num == ""): break
		try:
			print("讀入資料的倒數 = ",1/int(num))
		except IOError:
			print("\n*** 輸入資料檔不存在 ***\n")
		except ValueError:
			print("\n*** 偵測到非整數的字符，請輸入整數 ***\n")
		except ZeroDivisionError:
			print("\n*** 發生除0錯誤，輸入不能為0 ***\n")
		except KeyboardInterrupt:
			print("\n\n你按了^C或^Break鍵將迫使程式關閉\n")
			exit(0)
		except:
			print("發生其他異常")
		#else:
		#	print("\n讀檔+資料轉換順利，未發生預期的例外\n")
		finally:
		    print("\n已處理一輪，再接再厲\n")
	inputFile.close()
'''
