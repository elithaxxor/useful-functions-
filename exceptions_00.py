
    except subprocess.CalledProcessError as sub0:
        traceback.print_exc()
        print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub0)}')
    except subprocess.TimeoutExpired as sub1:
        traceback.print_exc()
        print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub1)}')
    except subprocess.SubprocessError as sub2:
        traceback.print_exc()
        print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub2)}')
        
        
    except EOFError as EOF:
        traceback.print_exc()
        print(str(EOF))
        print(f'{red}**Error, must have input{reset}')
    except Exception as e:
        traceback.print_exc()
        print(str(e))
        sys.exit(1)

        
        
        
except IOError as e:
    traceback.print_exc()
    print(f'{red}IO ERROR in parsing listdir()): {reset}', e)
    
    
 except KeyboardInterrupt:  ### keyboard interupt --> disable monitormode
  print(f'\n{red}[SYSTEM] USER EXIT.{reset}')
    traceback.print_exc()
            
