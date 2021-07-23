module.exports = function (grunt) {

  var config = {

    typescript: {
      base: {
        src: ['src/**/*.ts'],
        dest: 'lib',
        options: {
          module: 'commonjs', // commonjs or amd
          target: 'es5',      // es3 or es5
          basePath: 'src',
          sourceMap: true,
          declaration: true
        }
      }
    },

    coffee: {
      compile: {
        files: {
          'example.js':                  ['src/example.coffee'],
          'test/counter_hash_test.js':   ['src/test/counter_hash_test.coffee']
        }
      }
    },

    mocha_istanbul: {
      coverage: {
        src: 'test', // the folder, not the files
        options: {
          coverageFolder: 'coverage',
          mask: '**/*_test.js',
          root: '/',
          mochaOptions: { slow: 200 }
        }
      }
    }

  };

  grunt.initConfig(config);
  grunt.loadNpmTasks('grunt-typescript');
  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-mocha-istanbul');
  grunt.registerTask('test', [ 'mocha_istanbul:coverage' ]);
  grunt.registerTask('default', [ 'coffee', 'typescript' ]);
};
