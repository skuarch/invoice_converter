import src.file_service.file_service as file_service


def main():  
   
    # configure logs  
   
    print('Bienvenido al convertidor de facturas a csv')
    file_path = str(input('archivo a procesar: '))   
    print(f'procesando archivo: {file_path}')
    
    file_service.check_ext(file_path)
    
    xmls = file_service.extract_all(file_path)
    
    
    

if __name__ == '__main__':
    main()