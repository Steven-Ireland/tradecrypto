package tradecrypto

import com.linkedin.gradle.python.plugin.PythonSourceDistributionPlugin
import org.gradle.api.Plugin
import org.gradle.api.Project

class PythonPlugin implements Plugin<Project> {

    void apply(Project project) {
        project.plugins.apply(PythonSourceDistributionPlugin)
        project.repositories { pyGradlePyPi() }

//        project.dependencies {

//        }

/*	
	plugins {
  id "com.linkedin.python-sdist" version "0.4.9"
}

dependencies {
    python 'pypi:requests:2.9.1'
    test 'pypi:mock:1.3.0'
}

repositories {
   pyGradlePyPi()
}
	*/
    }

}
