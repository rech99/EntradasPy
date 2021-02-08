from OpenGL.GL import *
from glew_wish import *
import glfw

pos_x_triangulo = 0
pos_y_triangulo = 0

def dibujar():
    global pos_x_triangulo
    global pos_y_triangulo
    #rutinas de dibujo
    glPushMatrix()
    glTranslate(pos_x_triangulo, pos_y_triangulo, 0)
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0.1, 0)
    glVertex3f(-0.1, -0.1, 0)
    glVertex3f(0.1, -0.1, 0)
    glEnd()
    glPopMatrix()

def key_callback(window, key, scancode, action, mods):
    global pos_x_triangulo
    global pos_y_triangulo
    #Press, release, repeat
    #if key == glfw.KEY_ESCAPE:
    #    if action == glfw.PRESS:
    #       print("Se detecto un press de la tecla escape")
    #    if action == glfw.RELEASE:
    #        print("Se detecto un release")
    #    if action == glfw.REPEAT:
    #        print("Se detecto un repeat de la tecla escape")

    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, 1)

    if key == glfw.KEY_LEFT and action == glfw.PRESS:
        pos_x_triangulo = pos_x_triangulo -.05

    if key == glfw.KEY_RIGHT and action == glfw.PRESS:
        pos_x_triangulo = pos_x_triangulo + .05

    if key == glfw.KEY_DOWN and action == glfw.PRESS:
        pos_y_triangulo = pos_y_triangulo -.05

    if key == glfw.KEY_UP and action == glfw.PRESS:
        pos_y_triangulo = pos_y_triangulo + .05



def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    #Establecemos callback de evento de teclado
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.4,0.8,0.1,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()