/* File: fortfunctionsmodule.c
 * This file is auto-generated with f2py (version:1.21.6).
 * f2py is a Fortran to Python Interface Generator (FPIG), Second Edition,
 * written by Pearu Peterson <pearu@cens.ioc.ee>.
 * Generation date: Thu Dec 22 15:47:46 2022
 * Do not edit this file directly unless you know what you are doing!!!
 */

#ifdef __cplusplus
extern "C" {
#endif

/*********************** See f2py2e/cfuncs.py: includes ***********************/
#include "Python.h"
#include <stdarg.h>
#include "fortranobject.h"
#include <math.h>

/**************** See f2py2e/rules.py: mod_rules['modulebody'] ****************/
static PyObject *fortfunctions_error;
static PyObject *fortfunctions_module;

/*********************** See f2py2e/cfuncs.py: typedefs ***********************/
/*need_typedefs*/

/****************** See f2py2e/cfuncs.py: typedefs_generated ******************/
/*need_typedefs_generated*/

/********************** See f2py2e/cfuncs.py: cppmacros **********************/
#define rank(var) var ## _Rank
#define shape(var,dim) var ## _Dims[dim]
#define old_rank(var) (PyArray_NDIM((PyArrayObject *)(capi_ ## var ## _tmp)))
#define old_shape(var,dim) PyArray_DIM(((PyArrayObject *)(capi_ ## var ## _tmp)),dim)
#define fshape(var,dim) shape(var,rank(var)-dim-1)
#define len(var) shape(var,0)
#define flen(var) fshape(var,0)
#define old_size(var) PyArray_SIZE((PyArrayObject *)(capi_ ## var ## _tmp))
/* #define index(i) capi_i ## i */
#define slen(var) capi_ ## var ## _len
#define size(var, ...) f2py_size((PyArrayObject *)(capi_ ## var ## _tmp), ## __VA_ARGS__, -1)

#define CHECKSCALAR(check,tcheck,name,show,var)\
    if (!(check)) {\
        char errstring[256];\
        sprintf(errstring, "%s: "show, "("tcheck") failed for "name, var);\
        PyErr_SetString(fortfunctions_error,errstring);\
        /*goto capi_fail;*/\
    } else 
#ifdef DEBUGCFUNCS
#define CFUNCSMESS(mess) fprintf(stderr,"debug-capi:"mess);
#define CFUNCSMESSPY(mess,obj) CFUNCSMESS(mess) \
    PyObject_Print((PyObject *)obj,stderr,Py_PRINT_RAW);\
    fprintf(stderr,"\n");
#else
#define CFUNCSMESS(mess)
#define CFUNCSMESSPY(mess,obj)
#endif

#ifndef max
#define max(a,b) ((a > b) ? (a) : (b))
#endif
#ifndef min
#define min(a,b) ((a < b) ? (a) : (b))
#endif
#ifndef MAX
#define MAX(a,b) ((a > b) ? (a) : (b))
#endif
#ifndef MIN
#define MIN(a,b) ((a < b) ? (a) : (b))
#endif

#if defined(PREPEND_FORTRAN)
#if defined(NO_APPEND_FORTRAN)
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) _##F
#else
#define F_FUNC(f,F) _##f
#endif
#else
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) _##F##_
#else
#define F_FUNC(f,F) _##f##_
#endif
#endif
#else
#if defined(NO_APPEND_FORTRAN)
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) F
#else
#define F_FUNC(f,F) f
#endif
#else
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) F##_
#else
#define F_FUNC(f,F) f##_
#endif
#endif
#endif
#if defined(UNDERSCORE_G77)
#define F_FUNC_US(f,F) F_FUNC(f##_,F##_)
#else
#define F_FUNC_US(f,F) F_FUNC(f,F)
#endif


/************************ See f2py2e/cfuncs.py: cfuncs ************************/
static int f2py_size(PyArrayObject* var, ...)
{
  npy_int sz = 0;
  npy_int dim;
  npy_int rank;
  va_list argp;
  va_start(argp, var);
  dim = va_arg(argp, npy_int);
  if (dim==-1)
    {
      sz = PyArray_SIZE(var);
    }
  else
    {
      rank = PyArray_NDIM(var);
      if (dim>=1 && dim<=rank)
        sz = PyArray_DIM(var, dim-1);
      else
        fprintf(stderr, "f2py_size: 2nd argument value=%d fails to satisfy 1<=value<=%d. Result will be 0.\n", dim, rank);
    }
  va_end(argp);
  return sz;
}

static int
double_from_pyobj(double* v, PyObject *obj, const char *errmess)
{
    PyObject* tmp = NULL;
    if (PyFloat_Check(obj)) {
        *v = PyFloat_AsDouble(obj);
        return !(*v == -1.0 && PyErr_Occurred());
    }

    tmp = PyNumber_Float(obj);
    if (tmp) {
        *v = PyFloat_AsDouble(tmp);
        Py_DECREF(tmp);
        return !(*v == -1.0 && PyErr_Occurred());
    }

    if (PyComplex_Check(obj)) {
        PyErr_Clear();
        tmp = PyObject_GetAttrString(obj,"real");
    }
    else if (PyBytes_Check(obj) || PyUnicode_Check(obj)) {
        /*pass*/;
    }
    else if (PySequence_Check(obj)) {
        PyErr_Clear();
        tmp = PySequence_GetItem(obj, 0);
    }

    if (tmp) {
        if (double_from_pyobj(v,tmp,errmess)) {Py_DECREF(tmp); return 1;}
        Py_DECREF(tmp);
    }
    {
        PyObject* err = PyErr_Occurred();
        if (err==NULL) err = fortfunctions_error;
        PyErr_SetString(err,errmess);
    }
    return 0;
}

static int
int_from_pyobj(int* v, PyObject *obj, const char *errmess)
{
    PyObject* tmp = NULL;

    if (PyLong_Check(obj)) {
        *v = Npy__PyLong_AsInt(obj);
        return !(*v == -1 && PyErr_Occurred());
    }

    tmp = PyNumber_Long(obj);
    if (tmp) {
        *v = Npy__PyLong_AsInt(tmp);
        Py_DECREF(tmp);
        return !(*v == -1 && PyErr_Occurred());
    }

    if (PyComplex_Check(obj)) {
        PyErr_Clear();
        tmp = PyObject_GetAttrString(obj,"real");
    }
    else if (PyBytes_Check(obj) || PyUnicode_Check(obj)) {
        /*pass*/;
    }
    else if (PySequence_Check(obj)) {
        PyErr_Clear();
        tmp = PySequence_GetItem(obj, 0);
    }

    if (tmp) {
        if (int_from_pyobj(v, tmp, errmess)) {
            Py_DECREF(tmp);
            return 1;
        }
        Py_DECREF(tmp);
    }

    {
        PyObject* err = PyErr_Occurred();
        if (err == NULL) {
            err = fortfunctions_error;
        }
        PyErr_SetString(err, errmess);
    }
    return 0;
}


/********************* See f2py2e/cfuncs.py: userincludes *********************/
/*need_userincludes*/

/********************* See f2py2e/capi_rules.py: usercode *********************/


/* See f2py2e/rules.py */
/*eof externroutines*/

/******************** See f2py2e/capi_rules.py: usercode1 ********************/


/******************* See f2py2e/cb_rules.py: buildcallback *******************/
/*need_callbacks*/

/*********************** See f2py2e/rules.py: buildapi ***********************/

/************************* construct_abundance_matrix *************************/
static char doc_f2py_rout_fortfunctions_functionspy_construct_abundance_matrix[] = "\
matrix,b = construct_abundance_matrix(simg,femg,ymgi,ysii,xih2oi,xifei,xialsii,xialmgi,additional,[n_mats])\n\nWrapper for ``construct_abundance_matrix``.\
\n\nParameters\n----------\n"
"simg : input float\n"
"femg : input float\n"
"ymgi : input rank-1 array('i') with bounds (n_mats)\n"
"ysii : input rank-1 array('i') with bounds (n_mats)\n"
"xih2oi : input rank-1 array('d') with bounds (n_mats)\n"
"xifei : input rank-1 array('d') with bounds (n_mats)\n"
"xialsii : input rank-1 array('d') with bounds (n_mats)\n"
"xialmgi : input rank-1 array('d') with bounds (n_mats)\n"
"additional : input rank-1 array('d') with bounds (f2py_additional_d0)\n"
"\nOther Parameters\n----------------\n"
"n_mats : input int, optional\n    Default: len(ymgi)\n"
"\nReturns\n-------\n"
"matrix : rank-2 array('d') with bounds (n_mats,n_mats)\n"
"b : rank-2 array('d') with bounds (f2py_b_d0,f2py_b_d1)";
/* #declfortranroutine# */
static PyObject *f2py_rout_fortfunctions_functionspy_construct_abundance_matrix(const PyObject *capi_self,
                           PyObject *capi_args,
                           PyObject *capi_keywds,
                           void (*f2py_func)(double*,double*,int*,int*,int*,double*,double*,double*,double*,double*,double*,double*,int*,int*,int*)) {
    PyObject * volatile capi_buildvalue = NULL;
    volatile int f2py_success = 1;
/*decl*/

  double simg = 0;
  PyObject *simg_capi = Py_None;
  double femg = 0;
  PyObject *femg_capi = Py_None;
  int n_mats = 0;
  PyObject *n_mats_capi = Py_None;
  int *ymgi = NULL;
  npy_intp ymgi_Dims[1] = {-1};
  const int ymgi_Rank = 1;
  PyArrayObject *capi_ymgi_tmp = NULL;
  int capi_ymgi_intent = 0;
  PyObject *ymgi_capi = Py_None;
  int *ysii = NULL;
  npy_intp ysii_Dims[1] = {-1};
  const int ysii_Rank = 1;
  PyArrayObject *capi_ysii_tmp = NULL;
  int capi_ysii_intent = 0;
  PyObject *ysii_capi = Py_None;
  double *xih2oi = NULL;
  npy_intp xih2oi_Dims[1] = {-1};
  const int xih2oi_Rank = 1;
  PyArrayObject *capi_xih2oi_tmp = NULL;
  int capi_xih2oi_intent = 0;
  PyObject *xih2oi_capi = Py_None;
  double *matrix = NULL;
  npy_intp matrix_Dims[2] = {-1, -1};
  const int matrix_Rank = 2;
  PyArrayObject *capi_matrix_tmp = NULL;
  int capi_matrix_intent = 0;
  double *b = NULL;
  npy_intp b_Dims[2] = {-1, -1};
  const int b_Rank = 2;
  PyArrayObject *capi_b_tmp = NULL;
  int capi_b_intent = 0;
  double *xifei = NULL;
  npy_intp xifei_Dims[1] = {-1};
  const int xifei_Rank = 1;
  PyArrayObject *capi_xifei_tmp = NULL;
  int capi_xifei_intent = 0;
  PyObject *xifei_capi = Py_None;
  double *xialsii = NULL;
  npy_intp xialsii_Dims[1] = {-1};
  const int xialsii_Rank = 1;
  PyArrayObject *capi_xialsii_tmp = NULL;
  int capi_xialsii_intent = 0;
  PyObject *xialsii_capi = Py_None;
  double *xialmgi = NULL;
  npy_intp xialmgi_Dims[1] = {-1};
  const int xialmgi_Rank = 1;
  PyArrayObject *capi_xialmgi_tmp = NULL;
  int capi_xialmgi_intent = 0;
  PyObject *xialmgi_capi = Py_None;
  double *additional = NULL;
  npy_intp additional_Dims[1] = {-1};
  const int additional_Rank = 1;
  PyArrayObject *capi_additional_tmp = NULL;
  int capi_additional_intent = 0;
  PyObject *additional_capi = Py_None;
  int f2py_b_d0 = 0;
  int f2py_b_d1 = 0;
  int f2py_additional_d0 = 0;
    static char *capi_kwlist[] = {"simg","femg","ymgi","ysii","xih2oi","xifei","xialsii","xialmgi","additional","n_mats",NULL};

/*routdebugenter*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_clock();
#endif
    if (!PyArg_ParseTupleAndKeywords(capi_args,capi_keywds,\
        "OOOOOOOOO|O:fortfunctions.functionspy.construct_abundance_matrix",\
        capi_kwlist,&simg_capi,&femg_capi,&ymgi_capi,&ysii_capi,&xih2oi_capi,&xifei_capi,&xialsii_capi,&xialmgi_capi,&additional_capi,&n_mats_capi))
        return NULL;
/*frompyobj*/
  /* Processing variable ymgi */
  ;
  capi_ymgi_intent |= F2PY_INTENT_IN;
  capi_ymgi_tmp = array_from_pyobj(NPY_INT,ymgi_Dims,ymgi_Rank,capi_ymgi_intent,ymgi_capi);
  if (capi_ymgi_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 3rd argument `ymgi' of fortfunctions.functionspy.construct_abundance_matrix to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    ymgi = (int *)(PyArray_DATA(capi_ymgi_tmp));

  /* Processing variable additional */
  ;
  capi_additional_intent |= F2PY_INTENT_IN;
  capi_additional_tmp = array_from_pyobj(NPY_DOUBLE,additional_Dims,additional_Rank,capi_additional_intent,additional_capi);
  if (capi_additional_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 9th argument `additional' of fortfunctions.functionspy.construct_abundance_matrix to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    additional = (double *)(PyArray_DATA(capi_additional_tmp));

  /* Processing variable simg */
    f2py_success = double_from_pyobj(&simg,simg_capi,"fortfunctions.functionspy.construct_abundance_matrix() 1st argument (simg) can't be converted to double");
  if (f2py_success) {
  /* Processing variable femg */
    f2py_success = double_from_pyobj(&femg,femg_capi,"fortfunctions.functionspy.construct_abundance_matrix() 2nd argument (femg) can't be converted to double");
  if (f2py_success) {
  /* Processing variable b */
  ;
  capi_b_intent |= F2PY_INTENT_OUT|F2PY_INTENT_HIDE;
  capi_b_tmp = array_from_pyobj(NPY_DOUBLE,b_Dims,b_Rank,capi_b_intent,Py_None);
  if (capi_b_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting hidden `b' of fortfunctions.functionspy.construct_abundance_matrix to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    b = (double *)(PyArray_DATA(capi_b_tmp));

  /* Processing variable n_mats */
  if (n_mats_capi == Py_None) n_mats = len(ymgi); else
    f2py_success = int_from_pyobj(&n_mats,n_mats_capi,"fortfunctions.functionspy.construct_abundance_matrix() 1st keyword (n_mats) can't be converted to int");
  if (f2py_success) {
  CHECKSCALAR(len(ymgi)>=n_mats,"len(ymgi)>=n_mats","1st keyword n_mats","construct_abundance_matrix:n_mats=%d",n_mats) {
  /* Processing variable ysii */
  ysii_Dims[0]=n_mats;
  capi_ysii_intent |= F2PY_INTENT_IN;
  capi_ysii_tmp = array_from_pyobj(NPY_INT,ysii_Dims,ysii_Rank,capi_ysii_intent,ysii_capi);
  if (capi_ysii_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 4th argument `ysii' of fortfunctions.functionspy.construct_abundance_matrix to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    ysii = (int *)(PyArray_DATA(capi_ysii_tmp));

  /* Processing variable xih2oi */
  xih2oi_Dims[0]=n_mats;
  capi_xih2oi_intent |= F2PY_INTENT_IN;
  capi_xih2oi_tmp = array_from_pyobj(NPY_DOUBLE,xih2oi_Dims,xih2oi_Rank,capi_xih2oi_intent,xih2oi_capi);
  if (capi_xih2oi_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 5th argument `xih2oi' of fortfunctions.functionspy.construct_abundance_matrix to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    xih2oi = (double *)(PyArray_DATA(capi_xih2oi_tmp));

  /* Processing variable xialsii */
  xialsii_Dims[0]=n_mats;
  capi_xialsii_intent |= F2PY_INTENT_IN;
  capi_xialsii_tmp = array_from_pyobj(NPY_DOUBLE,xialsii_Dims,xialsii_Rank,capi_xialsii_intent,xialsii_capi);
  if (capi_xialsii_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 7th argument `xialsii' of fortfunctions.functionspy.construct_abundance_matrix to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    xialsii = (double *)(PyArray_DATA(capi_xialsii_tmp));

  /* Processing variable xialmgi */
  xialmgi_Dims[0]=n_mats;
  capi_xialmgi_intent |= F2PY_INTENT_IN;
  capi_xialmgi_tmp = array_from_pyobj(NPY_DOUBLE,xialmgi_Dims,xialmgi_Rank,capi_xialmgi_intent,xialmgi_capi);
  if (capi_xialmgi_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 8th argument `xialmgi' of fortfunctions.functionspy.construct_abundance_matrix to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    xialmgi = (double *)(PyArray_DATA(capi_xialmgi_tmp));

  /* Processing variable xifei */
  xifei_Dims[0]=n_mats;
  capi_xifei_intent |= F2PY_INTENT_IN;
  capi_xifei_tmp = array_from_pyobj(NPY_DOUBLE,xifei_Dims,xifei_Rank,capi_xifei_intent,xifei_capi);
  if (capi_xifei_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 6th argument `xifei' of fortfunctions.functionspy.construct_abundance_matrix to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    xifei = (double *)(PyArray_DATA(capi_xifei_tmp));

  /* Processing variable matrix */
  matrix_Dims[0]=n_mats,matrix_Dims[1]=n_mats;
  capi_matrix_intent |= F2PY_INTENT_OUT|F2PY_INTENT_HIDE;
  capi_matrix_tmp = array_from_pyobj(NPY_DOUBLE,matrix_Dims,matrix_Rank,capi_matrix_intent,Py_None);
  if (capi_matrix_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting hidden `matrix' of fortfunctions.functionspy.construct_abundance_matrix to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    matrix = (double *)(PyArray_DATA(capi_matrix_tmp));

  /* Processing variable f2py_b_d0 */
  f2py_b_d0 = shape(b, 0);
  /* Processing variable f2py_b_d1 */
  f2py_b_d1 = shape(b, 1);
  /* Processing variable f2py_additional_d0 */
  f2py_additional_d0 = shape(additional, 0);
/*end of frompyobj*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_call_clock();
#endif
/*callfortranroutine*/
  (*f2py_func)(&simg,&femg,&n_mats,ymgi,ysii,xih2oi,matrix,b,xifei,xialsii,xialmgi,additional,&f2py_b_d0,&f2py_b_d1,&f2py_additional_d0);
if (PyErr_Occurred())
  f2py_success = 0;
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_call_clock();
#endif
/*end of callfortranroutine*/
        if (f2py_success) {
/*pyobjfrom*/
/*end of pyobjfrom*/
        CFUNCSMESS("Building return value.\n");
        capi_buildvalue = Py_BuildValue("NN",capi_matrix_tmp,capi_b_tmp);
/*closepyobjfrom*/
/*end of closepyobjfrom*/
        } /*if (f2py_success) after callfortranroutine*/
/*cleanupfrompyobj*/
  /* End of cleaning variable f2py_additional_d0 */
  /* End of cleaning variable f2py_b_d1 */
  /* End of cleaning variable f2py_b_d0 */
  }  /*if (capi_matrix_tmp == NULL) ... else of matrix*/
  /* End of cleaning variable matrix */
  if((PyObject *)capi_xifei_tmp!=xifei_capi) {
    Py_XDECREF(capi_xifei_tmp); }
  }  /*if (capi_xifei_tmp == NULL) ... else of xifei*/
  /* End of cleaning variable xifei */
  if((PyObject *)capi_xialmgi_tmp!=xialmgi_capi) {
    Py_XDECREF(capi_xialmgi_tmp); }
  }  /*if (capi_xialmgi_tmp == NULL) ... else of xialmgi*/
  /* End of cleaning variable xialmgi */
  if((PyObject *)capi_xialsii_tmp!=xialsii_capi) {
    Py_XDECREF(capi_xialsii_tmp); }
  }  /*if (capi_xialsii_tmp == NULL) ... else of xialsii*/
  /* End of cleaning variable xialsii */
  if((PyObject *)capi_xih2oi_tmp!=xih2oi_capi) {
    Py_XDECREF(capi_xih2oi_tmp); }
  }  /*if (capi_xih2oi_tmp == NULL) ... else of xih2oi*/
  /* End of cleaning variable xih2oi */
  if((PyObject *)capi_ysii_tmp!=ysii_capi) {
    Py_XDECREF(capi_ysii_tmp); }
  }  /*if (capi_ysii_tmp == NULL) ... else of ysii*/
  /* End of cleaning variable ysii */
  } /*CHECKSCALAR(len(ymgi)>=n_mats)*/
  } /*if (f2py_success) of n_mats*/
  /* End of cleaning variable n_mats */
  }  /*if (capi_b_tmp == NULL) ... else of b*/
  /* End of cleaning variable b */
  } /*if (f2py_success) of femg*/
  /* End of cleaning variable femg */
  } /*if (f2py_success) of simg*/
  /* End of cleaning variable simg */
  if((PyObject *)capi_additional_tmp!=additional_capi) {
    Py_XDECREF(capi_additional_tmp); }
  }  /*if (capi_additional_tmp == NULL) ... else of additional*/
  /* End of cleaning variable additional */
  if((PyObject *)capi_ymgi_tmp!=ymgi_capi) {
    Py_XDECREF(capi_ymgi_tmp); }
  }  /*if (capi_ymgi_tmp == NULL) ... else of ymgi*/
  /* End of cleaning variable ymgi */
/*end of cleanupfrompyobj*/
    if (capi_buildvalue == NULL) {
/*routdebugfailure*/
    } else {
/*routdebugleave*/
    }
    CFUNCSMESS("Freeing memory.\n");
/*freemem*/
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_clock();
#endif
    return capi_buildvalue;
}
/********************* end of construct_abundance_matrix *********************/

/************************** compute_abundance_vector **************************/
static char doc_f2py_rout_fortfunctions_functionspy_compute_abundance_vector[] = "\
abundances = compute_abundance_vector(simg,femg,ymgi,ysii,xih2oi,xifei,xialsii,xialmgi,contents,[n_mats,additional])\n\nWrapper for ``compute_abundance_vector``.\
\n\nParameters\n----------\n"
"simg : input float\n"
"femg : input float\n"
"ymgi : input rank-1 array('i') with bounds (n_mats)\n"
"ysii : input rank-1 array('i') with bounds (n_mats)\n"
"xih2oi : input rank-1 array('d') with bounds (n_mats)\n"
"xifei : input rank-1 array('d') with bounds (n_mats)\n"
"xialsii : input rank-1 array('d') with bounds (n_mats)\n"
"xialmgi : input rank-1 array('d') with bounds (n_mats)\n"
"contents : input rank-1 array('i') with bounds (n_mats)\n"
"\nOther Parameters\n----------------\n"
"n_mats : input int, optional\n    Default: len(ymgi)\n"
"additional : input rank-1 array('d') with bounds (f2py_additional_d0)\n"
"\nReturns\n-------\n"
"abundances : rank-1 array('d') with bounds (n_mats)";
/* #declfortranroutine# */
static PyObject *f2py_rout_fortfunctions_functionspy_compute_abundance_vector(const PyObject *capi_self,
                           PyObject *capi_args,
                           PyObject *capi_keywds,
                           void (*f2py_func)(double*,double*,int*,int*,int*,double*,double*,double*,double*,double*,int*,double*,int*)) {
    PyObject * volatile capi_buildvalue = NULL;
    volatile int f2py_success = 1;
/*decl*/

  double simg = 0;
  PyObject *simg_capi = Py_None;
  double femg = 0;
  PyObject *femg_capi = Py_None;
  int n_mats = 0;
  PyObject *n_mats_capi = Py_None;
  int *ymgi = NULL;
  npy_intp ymgi_Dims[1] = {-1};
  const int ymgi_Rank = 1;
  PyArrayObject *capi_ymgi_tmp = NULL;
  int capi_ymgi_intent = 0;
  PyObject *ymgi_capi = Py_None;
  int *ysii = NULL;
  npy_intp ysii_Dims[1] = {-1};
  const int ysii_Rank = 1;
  PyArrayObject *capi_ysii_tmp = NULL;
  int capi_ysii_intent = 0;
  PyObject *ysii_capi = Py_None;
  double *xih2oi = NULL;
  npy_intp xih2oi_Dims[1] = {-1};
  const int xih2oi_Rank = 1;
  PyArrayObject *capi_xih2oi_tmp = NULL;
  int capi_xih2oi_intent = 0;
  PyObject *xih2oi_capi = Py_None;
  double *xifei = NULL;
  npy_intp xifei_Dims[1] = {-1};
  const int xifei_Rank = 1;
  PyArrayObject *capi_xifei_tmp = NULL;
  int capi_xifei_intent = 0;
  PyObject *xifei_capi = Py_None;
  double *xialsii = NULL;
  npy_intp xialsii_Dims[1] = {-1};
  const int xialsii_Rank = 1;
  PyArrayObject *capi_xialsii_tmp = NULL;
  int capi_xialsii_intent = 0;
  PyObject *xialsii_capi = Py_None;
  double *xialmgi = NULL;
  npy_intp xialmgi_Dims[1] = {-1};
  const int xialmgi_Rank = 1;
  PyArrayObject *capi_xialmgi_tmp = NULL;
  int capi_xialmgi_intent = 0;
  PyObject *xialmgi_capi = Py_None;
  double *abundances = NULL;
  npy_intp abundances_Dims[1] = {-1};
  const int abundances_Rank = 1;
  PyArrayObject *capi_abundances_tmp = NULL;
  int capi_abundances_intent = 0;
  int *contents = NULL;
  npy_intp contents_Dims[1] = {-1};
  const int contents_Rank = 1;
  PyArrayObject *capi_contents_tmp = NULL;
  int capi_contents_intent = 0;
  PyObject *contents_capi = Py_None;
  double *additional = NULL;
  npy_intp additional_Dims[1] = {-1};
  const int additional_Rank = 1;
  PyArrayObject *capi_additional_tmp = NULL;
  int capi_additional_intent = 0;
  PyObject *additional_capi = Py_None;
  int f2py_additional_d0 = 0;
    static char *capi_kwlist[] = {"simg","femg","ymgi","ysii","xih2oi","xifei","xialsii","xialmgi","contents","n_mats","additional",NULL};

/*routdebugenter*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_clock();
#endif
    if (!PyArg_ParseTupleAndKeywords(capi_args,capi_keywds,\
        "OOOOOOOOO|OO:fortfunctions.functionspy.compute_abundance_vector",\
        capi_kwlist,&simg_capi,&femg_capi,&ymgi_capi,&ysii_capi,&xih2oi_capi,&xifei_capi,&xialsii_capi,&xialmgi_capi,&contents_capi,&n_mats_capi,&additional_capi))
        return NULL;
/*frompyobj*/
  /* Processing variable ymgi */
  ;
  capi_ymgi_intent |= F2PY_INTENT_IN;
  capi_ymgi_tmp = array_from_pyobj(NPY_INT,ymgi_Dims,ymgi_Rank,capi_ymgi_intent,ymgi_capi);
  if (capi_ymgi_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 3rd argument `ymgi' of fortfunctions.functionspy.compute_abundance_vector to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    ymgi = (int *)(PyArray_DATA(capi_ymgi_tmp));

  /* Processing variable simg */
    f2py_success = double_from_pyobj(&simg,simg_capi,"fortfunctions.functionspy.compute_abundance_vector() 1st argument (simg) can't be converted to double");
  if (f2py_success) {
  /* Processing variable femg */
    f2py_success = double_from_pyobj(&femg,femg_capi,"fortfunctions.functionspy.compute_abundance_vector() 2nd argument (femg) can't be converted to double");
  if (f2py_success) {
  /* Processing variable additional */
  ;
  capi_additional_intent |= F2PY_INTENT_IN|F2PY_OPTIONAL;
  capi_additional_tmp = array_from_pyobj(NPY_DOUBLE,additional_Dims,additional_Rank,capi_additional_intent,additional_capi);
  if (capi_additional_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 2nd keyword `additional' of fortfunctions.functionspy.compute_abundance_vector to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    additional = (double *)(PyArray_DATA(capi_additional_tmp));

  /* Processing variable n_mats */
  if (n_mats_capi == Py_None) n_mats = len(ymgi); else
    f2py_success = int_from_pyobj(&n_mats,n_mats_capi,"fortfunctions.functionspy.compute_abundance_vector() 1st keyword (n_mats) can't be converted to int");
  if (f2py_success) {
  CHECKSCALAR(len(ymgi)>=n_mats,"len(ymgi)>=n_mats","1st keyword n_mats","compute_abundance_vector:n_mats=%d",n_mats) {
  /* Processing variable ysii */
  ysii_Dims[0]=n_mats;
  capi_ysii_intent |= F2PY_INTENT_IN;
  capi_ysii_tmp = array_from_pyobj(NPY_INT,ysii_Dims,ysii_Rank,capi_ysii_intent,ysii_capi);
  if (capi_ysii_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 4th argument `ysii' of fortfunctions.functionspy.compute_abundance_vector to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    ysii = (int *)(PyArray_DATA(capi_ysii_tmp));

  /* Processing variable contents */
  contents_Dims[0]=n_mats;
  capi_contents_intent |= F2PY_INTENT_IN;
  capi_contents_tmp = array_from_pyobj(NPY_INT,contents_Dims,contents_Rank,capi_contents_intent,contents_capi);
  if (capi_contents_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 9th argument `contents' of fortfunctions.functionspy.compute_abundance_vector to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    contents = (int *)(PyArray_DATA(capi_contents_tmp));

  /* Processing variable xih2oi */
  xih2oi_Dims[0]=n_mats;
  capi_xih2oi_intent |= F2PY_INTENT_IN;
  capi_xih2oi_tmp = array_from_pyobj(NPY_DOUBLE,xih2oi_Dims,xih2oi_Rank,capi_xih2oi_intent,xih2oi_capi);
  if (capi_xih2oi_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 5th argument `xih2oi' of fortfunctions.functionspy.compute_abundance_vector to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    xih2oi = (double *)(PyArray_DATA(capi_xih2oi_tmp));

  /* Processing variable xialsii */
  xialsii_Dims[0]=n_mats;
  capi_xialsii_intent |= F2PY_INTENT_IN;
  capi_xialsii_tmp = array_from_pyobj(NPY_DOUBLE,xialsii_Dims,xialsii_Rank,capi_xialsii_intent,xialsii_capi);
  if (capi_xialsii_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 7th argument `xialsii' of fortfunctions.functionspy.compute_abundance_vector to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    xialsii = (double *)(PyArray_DATA(capi_xialsii_tmp));

  /* Processing variable xialmgi */
  xialmgi_Dims[0]=n_mats;
  capi_xialmgi_intent |= F2PY_INTENT_IN;
  capi_xialmgi_tmp = array_from_pyobj(NPY_DOUBLE,xialmgi_Dims,xialmgi_Rank,capi_xialmgi_intent,xialmgi_capi);
  if (capi_xialmgi_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 8th argument `xialmgi' of fortfunctions.functionspy.compute_abundance_vector to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    xialmgi = (double *)(PyArray_DATA(capi_xialmgi_tmp));

  /* Processing variable xifei */
  xifei_Dims[0]=n_mats;
  capi_xifei_intent |= F2PY_INTENT_IN;
  capi_xifei_tmp = array_from_pyobj(NPY_DOUBLE,xifei_Dims,xifei_Rank,capi_xifei_intent,xifei_capi);
  if (capi_xifei_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting 6th argument `xifei' of fortfunctions.functionspy.compute_abundance_vector to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    xifei = (double *)(PyArray_DATA(capi_xifei_tmp));

  /* Processing variable abundances */
  abundances_Dims[0]=n_mats;
  capi_abundances_intent |= F2PY_INTENT_OUT|F2PY_INTENT_HIDE;
  capi_abundances_tmp = array_from_pyobj(NPY_DOUBLE,abundances_Dims,abundances_Rank,capi_abundances_intent,Py_None);
  if (capi_abundances_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : fortfunctions_error,"failed in converting hidden `abundances' of fortfunctions.functionspy.compute_abundance_vector to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    abundances = (double *)(PyArray_DATA(capi_abundances_tmp));

  /* Processing variable f2py_additional_d0 */
  f2py_additional_d0 = shape(additional, 0);
/*end of frompyobj*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_call_clock();
#endif
/*callfortranroutine*/
  (*f2py_func)(&simg,&femg,&n_mats,ymgi,ysii,xih2oi,xifei,xialsii,xialmgi,abundances,contents,additional,&f2py_additional_d0);
if (PyErr_Occurred())
  f2py_success = 0;
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_call_clock();
#endif
/*end of callfortranroutine*/
        if (f2py_success) {
/*pyobjfrom*/
/*end of pyobjfrom*/
        CFUNCSMESS("Building return value.\n");
        capi_buildvalue = Py_BuildValue("N",capi_abundances_tmp);
/*closepyobjfrom*/
/*end of closepyobjfrom*/
        } /*if (f2py_success) after callfortranroutine*/
/*cleanupfrompyobj*/
  /* End of cleaning variable f2py_additional_d0 */
  }  /*if (capi_abundances_tmp == NULL) ... else of abundances*/
  /* End of cleaning variable abundances */
  if((PyObject *)capi_xifei_tmp!=xifei_capi) {
    Py_XDECREF(capi_xifei_tmp); }
  }  /*if (capi_xifei_tmp == NULL) ... else of xifei*/
  /* End of cleaning variable xifei */
  if((PyObject *)capi_xialmgi_tmp!=xialmgi_capi) {
    Py_XDECREF(capi_xialmgi_tmp); }
  }  /*if (capi_xialmgi_tmp == NULL) ... else of xialmgi*/
  /* End of cleaning variable xialmgi */
  if((PyObject *)capi_xialsii_tmp!=xialsii_capi) {
    Py_XDECREF(capi_xialsii_tmp); }
  }  /*if (capi_xialsii_tmp == NULL) ... else of xialsii*/
  /* End of cleaning variable xialsii */
  if((PyObject *)capi_xih2oi_tmp!=xih2oi_capi) {
    Py_XDECREF(capi_xih2oi_tmp); }
  }  /*if (capi_xih2oi_tmp == NULL) ... else of xih2oi*/
  /* End of cleaning variable xih2oi */
  if((PyObject *)capi_contents_tmp!=contents_capi) {
    Py_XDECREF(capi_contents_tmp); }
  }  /*if (capi_contents_tmp == NULL) ... else of contents*/
  /* End of cleaning variable contents */
  if((PyObject *)capi_ysii_tmp!=ysii_capi) {
    Py_XDECREF(capi_ysii_tmp); }
  }  /*if (capi_ysii_tmp == NULL) ... else of ysii*/
  /* End of cleaning variable ysii */
  } /*CHECKSCALAR(len(ymgi)>=n_mats)*/
  } /*if (f2py_success) of n_mats*/
  /* End of cleaning variable n_mats */
  if((PyObject *)capi_additional_tmp!=additional_capi) {
    Py_XDECREF(capi_additional_tmp); }
  }  /*if (capi_additional_tmp == NULL) ... else of additional*/
  /* End of cleaning variable additional */
  } /*if (f2py_success) of femg*/
  /* End of cleaning variable femg */
  } /*if (f2py_success) of simg*/
  /* End of cleaning variable simg */
  if((PyObject *)capi_ymgi_tmp!=ymgi_capi) {
    Py_XDECREF(capi_ymgi_tmp); }
  }  /*if (capi_ymgi_tmp == NULL) ... else of ymgi*/
  /* End of cleaning variable ymgi */
/*end of cleanupfrompyobj*/
    if (capi_buildvalue == NULL) {
/*routdebugfailure*/
    } else {
/*routdebugleave*/
    }
    CFUNCSMESS("Freeing memory.\n");
/*freemem*/
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_clock();
#endif
    return capi_buildvalue;
}
/********************** end of compute_abundance_vector **********************/
/*eof body*/

/******************* See f2py2e/f90mod_rules.py: buildhooks *******************/

static FortranDataDef f2py_functionspy_def[] = {
  {"construct_abundance_matrix",-1,{{-1}},0,NULL,(void *)f2py_rout_fortfunctions_functionspy_construct_abundance_matrix,doc_f2py_rout_fortfunctions_functionspy_construct_abundance_matrix},
  {"compute_abundance_vector",-1,{{-1}},0,NULL,(void *)f2py_rout_fortfunctions_functionspy_compute_abundance_vector,doc_f2py_rout_fortfunctions_functionspy_compute_abundance_vector},
  {NULL}
};

static void f2py_setup_functionspy(char *construct_abundance_matrix,char *compute_abundance_vector) {
  int i_f2py=0;
  f2py_functionspy_def[i_f2py++].data = construct_abundance_matrix;
  f2py_functionspy_def[i_f2py++].data = compute_abundance_vector;
}
extern void F_FUNC(f2pyinitfunctionspy,F2PYINITFUNCTIONSPY)(void (*)(char *,char *));
static void f2py_init_functionspy(void) {
  F_FUNC(f2pyinitfunctionspy,F2PYINITFUNCTIONSPY)(f2py_setup_functionspy);
}

/*need_f90modhooks*/

/************** See f2py2e/rules.py: module_rules['modulebody'] **************/

/******************* See f2py2e/common_rules.py: buildhooks *******************/

/*need_commonhooks*/

/**************************** See f2py2e/rules.py ****************************/

static FortranDataDef f2py_routine_defs[] = {

/*eof routine_defs*/
  {NULL}
};

static PyMethodDef f2py_module_methods[] = {

  {NULL,NULL}
};

static struct PyModuleDef moduledef = {
  PyModuleDef_HEAD_INIT,
  "fortfunctions",
  NULL,
  -1,
  f2py_module_methods,
  NULL,
  NULL,
  NULL,
  NULL
};

PyMODINIT_FUNC PyInit_fortfunctions(void) {
  int i;
  PyObject *m,*d, *s, *tmp;
  m = fortfunctions_module = PyModule_Create(&moduledef);
  Py_SET_TYPE(&PyFortran_Type, &PyType_Type);
  import_array();
  if (PyErr_Occurred())
    {PyErr_SetString(PyExc_ImportError, "can't initialize module fortfunctions (failed to import numpy)"); return m;}
  d = PyModule_GetDict(m);
  s = PyUnicode_FromString("1.21.6");
  PyDict_SetItemString(d, "__version__", s);
  Py_DECREF(s);
  s = PyUnicode_FromString(
    "This module 'fortfunctions' is auto-generated with f2py (version:1.21.6).\nFunctions:\n"
"Fortran 90/95 modules:\n""  functionspy --- construct_abundance_matrix(),compute_abundance_vector()"".");
  PyDict_SetItemString(d, "__doc__", s);
  Py_DECREF(s);
  s = PyUnicode_FromString("1.21.6");
  PyDict_SetItemString(d, "__f2py_numpy_version__", s);
  Py_DECREF(s);
  fortfunctions_error = PyErr_NewException ("fortfunctions.error", NULL, NULL);
  /*
   * Store the error object inside the dict, so that it could get deallocated.
   * (in practice, this is a module, so it likely will not and cannot.)
   */
  PyDict_SetItemString(d, "_fortfunctions_error", fortfunctions_error);
  Py_DECREF(fortfunctions_error);
  for(i=0;f2py_routine_defs[i].name!=NULL;i++) {
    tmp = PyFortranObject_NewAsAttr(&f2py_routine_defs[i]);
    PyDict_SetItemString(d, f2py_routine_defs[i].name, tmp);
    Py_DECREF(tmp);
  }


/*eof initf2pywraphooks*/
  PyDict_SetItemString(d, "functionspy", PyFortranObject_New(f2py_functionspy_def,f2py_init_functionspy));
/*eof initf90modhooks*/

/*eof initcommonhooks*/


#ifdef F2PY_REPORT_ATEXIT
  if (! PyErr_Occurred())
    on_exit(f2py_report_on_exit,(void*)"fortfunctions");
#endif
  return m;
}
#ifdef __cplusplus
}
#endif
