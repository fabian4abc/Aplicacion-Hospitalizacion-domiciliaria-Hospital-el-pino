import React, { Component } from 'react'
import {createStackNavigator } from 'react-navigation-stack'
import {Text} from 'react-native'
import Login from './components/login'
import Home from './components/home'
import Perfil from './components/perfil'
import EditarPerfil from './components/editarperfil'
import VisitasAsignadas from './components/visitasAsignadas'
import Paciente from './components/paciente'
import Visita from './components/visita'
import Mapa from './components/mapa'
import Detallevisita from './components/detallesvisita'
import Visitasantiguas from './components/visitasantiguas'
import { createAppContainer } from 'react-navigation';


const AppNavigator = createStackNavigator({
  Login : {
    screen : Login
  },
  Home : {
    screen : Home
  },
  Perfil : {
    screen : Perfil
  },
  EditarPerfil : {
    screen : EditarPerfil
  },
  VisitasAsignadas : {
    screen : VisitasAsignadas
  },
  Paciente : {
    screen : Paciente
  },
  Visita : {
    screen : Visita
  },
  Mapa : {
    screen : Mapa
  },
  Detallevisita : {
    screen : Detallevisita
  },
  Visitasantiguas : {
    screen : Visitasantiguas
  }  
})

const App = createAppContainer(AppNavigator);
export default class Apps extends Component {
  render(){
    return(
      <App/>
    );
  }
}