Algoritmo TlaxReport
	//Elaborado por: Arisbeth
	Definir opc, contador, subopc, i, buscartipo Como Entero;
	Definir nombre, direc, descrip, tipoDenuncia Como Cadena;
	Definir buscarNombre, tipoabuscar Como Cadena;
	Definir encontrado Como Lógico;
	contador <- 0;
	Dimensionar nombre[100];
	Dimensionar direc[100];
	Dimensionar descrip[100];
	Dimensionar tipoDenuncia[100];
	Repetir
		Escribir '=====TlaxReport=====';
		Escribir 'Este es un programa para el registro de Denuncias ciudadanas';
		Escribir 'Elige el tipo de reporte que harás:';
		Escribir '1. Baches';
		Escribir '2. Alumbrado público';
		Escribir '3. Fuga de agua';
		Escribir '4. Semáforos';
		Escribir '5. Fuga de gas';
		Escribir '6. Mostrar todas las denuncias';
		Escribir '7. Buscar denuncia por nombre';
		Escribir '8. Buscar denuncia por tipo';
		Escribir '9. Salir';
		Leer opc;
		Según opc Hacer
			1:
		        contador <- contador+1;
				tipoDenuncia[contador] = "Baches";
				Escribir '====Reporte de Baches====';
				Escribir 'Ingrese su nombre completo';
				Leer nombre[contador];
				Escribir 'Ingrese la direccion';
				Leer direc[contador];
				Escribir 'Describa el problema:';
				Leer descrip[contador];
				Escribir 'Tu reporte ha sido guardado';
				Escribir 'Presionar una tecla para continuar...';
				Esperar Tecla;
			2:
				Escribir '====Reporte de Alumbrado público====';
				Escribir '¿Qué quieres reportar?';
				Escribir '1. Falta de Alumbrado público';
				Escribir '2. Mantenimiento de Alumbrado';
				Leer subopc;
				Según subopc Hacer
			        1:
				        contador <- contador+1;
						tipoDenuncia[contador] = "Falta de Alumbrado";
						Escribir '==Falta de Alumbrado==';
						Escribir 'Ingrese su nombre completo';
						Leer nombre[contador];
						Escribir 'Ingrese la direccion';
						Leer direc[contador];
						Escribir 'Describa el problema:';
						Leer descrip[contador];
						Escribir 'Tu reporte ha sido guardado';
						Escribir 'Presionar una tecla para continuar...';
						Esperar Tecla;
					2:
						contador <- contador+1;
						tipoDenuncia[contador] = "Mantenimiento de Alumbrado";
						Escribir '==Mantenimiento de Alumbrado==';
						Escribir 'Ingrese su nombre completo';
						Leer nombre[contador];
						Escribir 'Ingrese la direccion';
						Leer direc[contador];
						Escribir 'Describa el problema:';
						Leer descrip[contador];
						Escribir 'Tu reporte ha sido guardado';
						Escribir 'Presionar una tecla para continuar...';
						Esperar Tecla;
					De Otro Modo:
						Escribir 'Opcion no válida';
				FinSegún
				Escribir 'Presionar una tecla para continuar...';
				Esperar Tecla;
			3:
				contador <- contador+1;
				tipoDenuncia[contador] = "Fuga de agua";
				Escribir '====Reporte de Fuga de agua====';
				Escribir 'Ingrese su nombre completo';
				Leer nombre[contador];
				Escribir 'Ingrese la direccion';
				Leer direc[contador];
				Escribir 'Describa el problema:';
				Leer descrip[contador];
				Escribir 'Tu reporte ha sido guardado';
				Escribir 'Presionar una tecla para continuar...';
				Esperar Tecla;
			4:
				Escribir '====Reporte de Semáforos====';
				Escribir '¿Qué quieres reportar?';
				Escribir '1. Faltan Semáforos';
				Escribir '2. Mantenimiento de Semáforo';
				Leer subopc;
				Según subopc Hacer
			        1:
				        contador <- contador+1;
						tipoDenuncia[contador] = "Faltan Semáforos";
						Escribir '==Faltan Semáforos==';
						Escribir 'Ingrese su nombre completo';
						Leer nombre[contador];
						Escribir 'Ingrese la direccion';
						Leer direc[contador];
						Escribir 'Describa el problema:';
						Leer descrip[contador];
						Escribir 'Tu reporte ha sido guardado';
						Escribir 'Presionar una tecla para continuar...';
						Esperar Tecla;
					2:
						contador <- contador + 1;
						tipoDenuncia[contador] = "Mantenimiento de Semáforos";
						Escribir 'Ingrese su nombre completo';
						Leer nombre[contador];
						Escribir 'Ingrese la direccion';
						Leer direc[contador];
						Escribir 'Describa el problema:';
						Leer descrip[contador];
						Escribir 'Tu reporte ha sido guardado';
						Escribir 'Presionar una tecla para continuar...';
						Esperar Tecla;
					De Otro Modo:
						Escribir 'Opcion no válida';
				FinSegún
				Escribir 'Presionar una tecla para continuar...';
				Esperar Tecla;
			5:
				contador <- contador+1;
				tipoDenuncia[contador] = "Fuga de gas";
				Escribir '====Reporte de Fuga de gas====';
				Escribir 'Ingrese su nombre completo';
				Leer nombre[contador];
				Escribir 'Ingrese la direccion';
				Leer direc[contador];
				Escribir 'Describa el problema:';
				Leer descrip[contador];
				Escribir 'Tu reporte ha sido guardado';
				Escribir 'Presionar una tecla para continuar...';
				Esperar Tecla;
			6:
				Si contador=0 Entonces
					Escribir 'No hay denuncias registradas';
				SiNo
					Para i<-1 Hasta contador Hacer
						Escribir '===Denuncia', i, '===';
						Escribir 'Nombre: ', nombre[i];
						Escribir 'Dirección: ', direc[i];
						Escribir 'Descripción: ', descrip[i];
					FinPara
				FinSi
				Escribir 'Presionar una tecla para continuar...';
				Esperar Tecla;
			7:
				encontrado <- Falso;
				Escribir 'Ingrese el nombre a buscar:';
				Leer buscarNombre;
				Para i<-1 Hasta contador Hacer
					Si nombre[i]=buscarNombre Entonces
						encontrado <- Verdadero;
						Escribir 'Denuncia Encontrada';
						Escribir 'Nombre: ', nombre[i];
						Escribir 'Dirección: ', direc[i];
						Escribir 'Descripción: ', descrip[i];
					FinSi
				FinPara
				Si encontrado=Falso Entonces
					Escribir 'No se encontró ninguna denuncia';
				FinSi
				Escribir 'Presionar una tecla para continuar...';
				Esperar Tecla;
			8:
				encontrado <- Falso;
				Escribir 'Eliga el tipo de denuncia a buscar:';
				Escribir "1. Baches";
				Escribir "2. Falta de Alumbrado";
				Escribir "3. Mantenimiento de Alumbrado";
				Escribir "4. Fuga de agua";
				Escribir "5. Faltan Semáforos";
				Escribir "6. Mantenimiento de Semáforos";
				Escribir "7. Fuga de gas";
				Leer buscartipo;
				Segun buscartipo Hacer
					1:
						tipoabuscar <- "Baches";
					2:
						tipoabuscar <- "Falta de Alumbrado";
					3:
						tipoabuscar <- "Mantenimiento de Alumbrado";
					4:
						tipoabuscar <- "Fuga de agua";
					5:
						tipoabuscar <- "Faltan Semáforos";
					6:
						tipoabuscar <- "Mantenimiento de Semáforos";
					7:
						tipoabuscar <- "Fuga de gas";
					De Otro Modo:
						Escribir "Opción no válida";
				Fin Segun
				Para i<-1 Hasta contador Hacer
					Si tipoDenuncia[i]=tipoabuscar Entonces
						encontrado <- Verdadero;
						Escribir 'Denuncia Encontrada';
						Escribir 'Nombre: ', nombre[i];
						Escribir 'Dirección: ', direc[i];
						Escribir 'Descripción: ', descrip[i];
					FinSi
				FinPara
				Si encontrado=Falso Entonces
					Escribir 'No se encontraron denuncias';
				FinSi
				Escribir 'Presionar una tecla para continuar...';
				Esperar Tecla;
			9:
				Escribir 'Saliendo del Sistema...';
			De Otro Modo:
				Escribir 'Opcion no válida';
		FinSegún
	Hasta Que opc=9
FinAlgoritmo
