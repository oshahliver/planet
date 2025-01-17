# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:05:05 2018

@author: os18o068
"""

from picse.physicalparams import (
    T0_list,
    K0_list,
    K0prime_list,
    rho0_list,
    aP_list,
    molar_mass_list,
    Rgas,
    mH,
    mO,
    kB,
    G,
    EOS_type,
    material_list,
    EOSstring_list,
    NA,
    P_earth,
    m_earth,
    r_earth,
    material_plot_list,
    solar_system,
    abbrevations_solar,
    P_zero,
    T_zero,
    mFe,
    mMg,
    mSi,
    Mg_number_solar,
    Si_number_solar,
    mH2O,
    mBr,
    mPer,
    mOl,
    mEn,
    a_KD,
    b_KD,
    c_KD,
    mS,
    a_KDi,
    b_KDi,
    c_KDi,
    eki,
    bulk_DMM_lower_Workmann,
    mAl,
    mNi,
    mCa,
    y_oxides,
    bulk_DMM_upper_Workmann,
    bulk_DMM_Allegre,
    P_FeO_Fe_trans,
)

from picse.runparams import (
    eps_Psurf,
    eps_Mtot,
    eps_layer,
    param_colors,
    pressure_switch_H2O,
    color_list,
    xi_Fe_mantle_max,
)
import numpy as np

# import eosfort
import random
import matplotlib as mpl
import matplotlib.transforms as transforms
import time

# from picse.materials import phaseCheck
from picse.utils.function_tools import functionTools as ftool

# from picse.materials import eos
from matplotlib import pyplot as plt

# from picse.materials import brucite_phase
# from picse.materials import hydration
from decimal import Decimal
from picse.utils.plot_tools import plotTools
import scipy.integrate as integrate
from picse.materials import eos

import warnings

# from picse.materials import brucite_phase as bruce

# mpl.rc("text", usetex=True)
# mpl.rcParams["text.latex.preamble"] = r"\usepackage{amsmath, amssymb}"
warnings.filterwarnings("ignore")
plotPath = "/home/os18o068/Documents/PHD/Abbildungen/"


# class Sotin:
#     """
#     Basic implementation of the composition model by Sotin et al. 2007.
#     """

#     def __init__(self, MgSi=1.131, FeSi=0.986, Mg_number_Si=0.9):
#         self.MgSi = MgSi
#         self.Mg_number_Si = Mg_number_Si
#         self.Mg = None
#         self.Fe = None
#         self.Si = None
#         self.O = None
#         self.FeMg_Si = (1.0 - Mg_number_Si) / Mg_number_Si
#         self.FeMg = None
#         self.FeSi = FeSi
#         self.Fe_number_Si = (
#             (1 - Mg_number_Si)
#             / (Mg_number_Si)
#             / (1 + (1 - Mg_number_Si) / Mg_number_Si)
#         )
#         self.x3 = 2.0 * (1.0 - Mg_number_Si / MgSi)
#         self.y3 = 1.0 - Mg_number_Si

#     def getAbundances(self):
#         """Computes molar abundances of Mg, Si, Fe and O as a function of
#         the input ratio Mg/Si and the Mg# in the Silicates according to
#         Sotin 2007
#         """
#         Mg = 2 * (1.0 - self.y3)
#         Fe = 2 * self.y3
#         Si = 2.0 - self.x3
#         O = 6.0 - 2.0 * self.x3

#         tot = Mg + Fe + Si + O

#         self.Mg = Mg / tot
#         self.Fe = Fe / tot
#         self.Si = Si / tot
#         self.O = O / tot
#         self.FeMg = self.FeSi / self.MgSi

#         print("\n Mantle:")
#         print("\n Mg:", self.Mg, "\n Fe:", self.Fe, "\n Si:", self.Si, "\n O:", self.O)

#         print(" Fe/Mg silicates: ", self.FeMg_Si)
#         print(" Si/Mg silicates: ", 1.0 / self.MgSi)
#         print(" Fe# silicates:", self.Fe_number_Si)
#         print(" Si# silicates:", 1.0 / self.MgSi / (1.0 + 1.0 / self.MgSi))

#         print(" x3 =", self.x3)
#         print(" y3 =", self.y3)

#         print("\n Planet:")
#         print("\n Fe/Mg in planet:", self.FeMg)
#         print(" Mg# tot:", 1.0 / self.FeMg / (1.0 + 1.0 / self.FeMg))


# def plot_mantle_content(N=50):
#     path = "/home/os18o068/Documents/PHD/Abbildungen/"
#     pres = np.linspace(30e9, 70e9, N)

#     X_S = np.linspace(0.0, 0.1, 3)
#     X_Si = np.array([0.005, 0.0075, 0.01])
#     X_O = np.array([0.0005, 0.001, 0.002, 0.003, 0.004, 0.005])
#     linestyles = ["-", "--", "-.", ":"]

#     data = np.empty([len(X_S), len(X_Si), len(X_O), 2, len(pres)])

#     # prepare data
#     for i in range(len(X_S)):
#         for j in range(len(X_Si)):
#             for k in range(len(X_O)):
#                 for p in range(len(pres)):
#                     # convert material fractions to atomic abundances in the core
#                     xi = mat2at_core(
#                         xi=wt2mol(wt=[X_S[i], X_Si[j], X_O[k]], xiH=0.0), xiH=0.0
#                     )

#                     # compute Fe and Si content of the silicates from the
#                     # chemical partitioning model
#                     f = Fe_number_mantle(pres[p], T_liquidus_pyrolite(pres[p]), xi)
#                     s = Si_number_mantle(pres[p], T_liquidus_pyrolite(pres[p]), xi)

#                     if f <= 0.0 or f == xi_Fe_mantle_max:
#                         f = None

#                     data[i][j][k][0][p] = f
#                     data[i][j][k][1][p] = s

#     fig, ax = plt.subplots(len(X_S), 2, figsize=(10, 8))
#     fig.subplots_adjust(wspace=0.25)
#     plot_list1 = []
#     label_list1 = []
#     plot_list2 = []
#     label_list2 = []

#     bbox_props = dict(edgecolor="k", facecolor="white", linewidth=0.5)

#     ax[0][1].text(
#         0.4,
#         1.0,
#         r"$\rm Mantle \ composition$",
#         fontsize=20,
#         transform=ax[0][1].transAxes,
#         bbox=bbox_props,
#     )

#     fnts1 = 12
#     fnts2 = 14
#     for i in range(len(X_S)):
#         # ax[i][0].set_ylim(0., xi_Fe_mantle_max)
#         trafo = transforms.blended_transform_factory(
#             ax[i][0].transAxes, ax[i][0].transAxes
#         )

#         ax[i][0].set_ylabel(r"$\rm [FeO]/[FeO+MgO]$", fontsize=fnts2)
#         ax[i][1].set_ylabel(r"$\rm [SiO_2]/[SiO_2+MgO]$", fontsize=fnts2)
#         ax[i][0].text(
#             0.95,
#             0.85,
#             r"${}$".format(int(X_S[i] * 100)) + r"$\ {\rm wt}\% \ \rm S \ in \ core$",
#             transform=trafo,
#             bbox=bbox_props,
#             ha="right",
#             size=fnts2,
#         )

#         for j in range(len(X_Si)):
#             for k in range(len(X_O)):
#                 for l in range(2):
#                     ax[i][l].set_xlim(pres[0] * 1e-9, pres[-1] * 1e-9)
#                     ax[i][l].tick_params(labelsize=fnts2)
#                     color = color_list[-k * 2]
#                     try:
#                         if l == 0:
#                             (pl,) = ax[i][l].semilogy(
#                                 pres * 1e-9,
#                                 data[i][j][k][l],
#                                 color=color,
#                                 linestyle=linestyles[j],
#                             )
#                             # ax[i][0].set_ylim(0., .25)
#                             ax[i][l].set_ylim(0.003, 0.5)

#                         else:
#                             (pl,) = ax[i][l].plot(
#                                 pres * 1e-9,
#                                 data[i][j][k][l],
#                                 color=color,
#                                 linestyle=linestyles[j],
#                             )

#                             # ax[i][0].set_ylim(0., .25)
#                             ax[i][l].set_ylim(0.3, 0.6)

#                     except TypeError:
#                         if l == 0:
#                             (pl,) = ax[i][l].semilogy(
#                                 pres * 1e-9,
#                                 data[i][j][k][l],
#                                 color=color,
#                                 linestyle=linestyles[j],
#                             )
#                             # ax[i][0].set_ylim(0., .25)
#                             ax[i][l].set_ylim(0.003, 0.5)

#                         else:
#                             (pl,) = ax[i][l].plot(
#                                 pres * 1e-9,
#                                 data[i][j][k][l],
#                                 color=color,
#                                 linestyle=linestyles[j],
#                             )

#                             # ax[i][0].set_ylim(0., .25)
#                             ax[i][l].set_ylim(0.3, 0.6)

#                 if k == 0 and i == 0:
#                     plot_list2.append(pl)
#                     label_list2.append(
#                         r"${}$".format(str(round(X_Si[j] * 100, 3))) + r"$\ {\rm wt}\%$"
#                     )

#                 if j == 0 and i == 0:
#                     plot_list1.append(pl)
#                     label_list1.append(
#                         r"${}$".format(str(round(X_O[k] * 100, 3))) + r"$\ {\rm wt}\%$"
#                     )

#     try:
#         legend1 = ax[0][0].legend(
#             plot_list1, label_list1, loc=3, title=r"$\rm O \ in \ core$", fontsize=fnts1
#         )
#         ax[0][0].add_artist(legend1)
#         legend2 = ax[0][1].legend(
#             plot_list2,
#             label_list2,
#             loc=3,
#             title=r"$\rm Si \ in \ core$",
#             fontsize=fnts1,
#         )
#         legend1.get_title().set_fontsize(fnts1)
#         legend2.get_title().set_fontsize(fnts1)
#         legend1.get_frame().set_alpha(0.5)
#         legend2.get_frame().set_alpha(0.5)
#         ax[0][1].add_artist(legend2)
#         ax[-1][0].set_xlabel(
#             r"$\rm Core \ segregation \ pressure \ [GPa]$", fontsize=fnts2
#         )
#         ax[-1][1].set_xlabel(
#             r"$\rm Core \ segregation \ pressure \ [GPa]$", fontsize=fnts2
#         )

#     except TypeError:
#         legend1 = ax[0].legend(plot_list1, label_list1, loc=3, title="oxygen")
#         ax[0].add_artist(legend1)
#         ax[0].set_xlabel("Core segregation pressure [GPa]", fontsize=fnts2)
#         ax[1].set_xlabel("Core segregation pressure [GPa]", fontsize=fnts2)

#     fig.savefig(path + "mantle_composition.pdf", format="pdf", bbox_inches="tight")
#     plt.close(fig)


def density_mean(densities, fractions):
    """
    Compute the mean density of a mixture using the linear mixing law.

    Parameters:
    densities (list): List of individual densities.
    fractions (list): List of individual weight fractions.

    Returns:
    float: Mean density of the mixture.
    """

    return 1.0 / sum([f / d for d, f in zip(densities, fractions)])


def bulk_modulus_mean(densities, bulks, fractions, dens=None):
    """
    Compute the mean isothermal bulk modulus of a mixture using the linear mixing law.

    Parameters:
    densities (list): List of individual densities.
    bulks (list): List of individual isothermal bulk moduli.
    fractions (list): List of individual weight fractions.
    dens (float, optional): Mean density of mixture, Defaults to None.

    Returns:
    float: Mean isothermal bulk modulus of the mixture.
    """

    if not dens is None:
        return 1 / (
            dens * sum([f / d / k for (f, d, k) in zip(fractions, densities, bulks)])
        )

    else:
        return 1 / (
            density_mean(densities, fractions)
            * sum([f / d / k for (f, d, k) in zip(fractions, densities, bulks)])
        )


def thermal_expansion_mean(densities, alphas, fractions, dens=None):
    """
    Compute the mean thermal expansion coefficient of a mixture using the linear mixing law.

    Parameters:
    densities (list): List of individual densities.
    alphas (list): List of individual thermal expansion coefficients..
    fractions (list): List of individual weight fractions.
    dens (float, optional): Mean density of mixture, Defaults to None.

    Returns:
    float: Mean thermal expansion coefficient of the mixture.
    """
    if not dens is None:
        return dens * sum(
            [a * f / d for (a, f, d) in zip(alphas, fractions, densities)]
        )

    else:
        return density_mean(densities, fractions) * sum(
            [a * f / d for (a, f, d) in zip(alphas, fractions, densities)]
        )


def dPdrho_mean(densities, dPdrhos, fractions, dens=None):
    """
    Compute the mean density derivative of the pressure of a mixture using the linear mixing law.

    Parameters:
    densities (list): List of individual densities.
    alphas (list): List of individual thermal expansion coefficients..
    fractions (list): List of individual weight fractions.
    dens (float, optional): Mean density of mixture, Defaults to None.

    Returns:
    float: Mean density derivative of the pressure of the mixture.
    """
    if not dens is None:
        return 1.0 / (
            dens ** 2
            * sum(
                [
                    1 / d ** 2 * f / dp
                    for (dp, f, d) in zip(dPdrhos, fractions, densities)
                ]
            )
        )
    else:
        return 1.0 / (
            density_mean(densities, fractions) ** 2
            * sum(
                [
                    1 / d ** 2 * f / dp
                    for (dp, f, d) in zip(dPdrhos, fractions, densities)
                ]
            )
        )


def xi_general(eta, m):
    dummy = sum([eta[i] / m[i] for i in range(len(m))])
    y = np.array([eta[i] / m[i] / dummy for i in range(len(m))])
    print("sum =", sum(y))
    return y


def x_general(w, m):
    """
    Computes the mole fractions from the weight fractions and the molar masses.

    Parameters:
    w (list): weight fractions.
    m (list): molar masses.

    Returns:
    list: mole fractions.
    """
    dummy = sum([w[i] / m[i] for i in range(len(m))])
    y = np.array([eta[i] / m[i] / dummy for i in range(len(m))])
    return y


def wt2mol_oxides(wt=bulk_DMM_lower_Workmann, replace=True):
    """
    Compute bulk DMM composition for the Earth in terms of mol fractions of the
    most relevant oxides. By default the average of the data from Workmann 2005
    is taken. If replace: Ni -> Fe, Al -> Si, Ca -> Mg.
    """
    m = np.array(
        [mMg + mO, mSi + 2 * mO, mFe + mO, mCa + mO, 2 * mAl + 3 * mO, mNi + mO]
    )
    all_fracs = np.empty([len(m)])
    ox_fracs = np.empty([3])

    for i in range(len(m)):
        j = 0
        all_fracs[i] = wt[i] / wt[j] * y_oxides[i] / y_oxides[j] * m[j] / m[i]

    for i in range(len(ox_fracs)):
        if replace:
            fac = 1.0
        else:
            fac = 0.0

        ox_fracs[i] = all_fracs[i] + fac * all_fracs[i + 3]
        ox_fracs[i] /= sum(all_fracs)

    return ox_fracs


def at2mat(at):
    """Converts atomic mole fractions into material mole fractions. The composition
    of the different materials is given by the matrix N. This function is only valid
    for a composition of Fe, S, O, Si for the cores.
    """

    N = [
        [1.0, 1.0, 1.0, 1.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]

    # construct matrix
    matrix = np.zeros([len(at), len(at)])
    for i in range(len(at)):
        # compute row
        for j in range(len(at)):
            for k in range(len(at)):
                matrix[i][j] += N[k][j] * at[i]
            matrix[i][j] -= N[i][j]

    matrix[0] = np.ones(len(at))
    x = np.linalg.solve(matrix, np.array([1.0, 0.0, 0.0, 0.0]))

    return x


def at2mat_max(at):
    """Converts atomic mole fractions into material mole fractions. The composition
    of the different materials is given by the matrix N.
    """

    N = [
        [1.0, 1.0, 1.0, 1.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]

    # construct matrix
    matrix = np.zeros([len(at), len(at)])
    for i in range(len(at)):
        # compute row
        for j in range(len(at)):
            for k in range(len(at)):
                matrix[i][j] += N[k][j] * at[i]
            matrix[i][j] -= N[i][j]

    matrix[0] = np.ones(len(at))
    # matrix[0] = np.array([1., 0., 0., 0.])
    x = np.linalg.solve(matrix, np.array([1.0, 0.0, 0.0, 0.0]))
    print("x =", x)
    print("sum =", sum(x))

    if x[0] < 0e0:
        print(x[1:])
        x /= sum(x[1:])
        x[0] = 0.0

    print("sum =", sum(x))
    print("matrix =", matrix)
    return x


def matrix(wt=[0.25, 0.25, 0.25], xiH=0.0):
    mFeHx = (1 - xiH) * mFe + xiH * mH

    matrix = np.array(
        [
            [1.0, 1.0, 1.0, 1.0],
            [
                0.0,
                ((mFe + mS) * wt[0] - mS) - wt[0] * mFeHx,
                wt[0] * (mFe + mSi - mFeHx),
                wt[0] * (mFe + mO - mFeHx),
            ],
            [
                0.0,
                wt[1] * (mFe + mS - mFeHx),
                ((mFe + mSi) * wt[1] - mSi) - wt[1] * mFeHx,
                wt[1] * (mFe + mO - mFeHx),
            ],
            [
                0.0,
                wt[2] * (mFe + mS - mFeHx),
                wt[2] * (mFe + mSi - mFeHx),
                ((mFe + mO) * wt[2] - mO) - wt[2] * mFeHx,
            ],
        ]
    )

    return matrix


def wt2mol(wt=[0.25, 0.25, 0.25], xiH=0.0):
    """Give X_S, X_Si, X_O as wt frac and xiH in FeHx in mol frac to compute
    the mol fracs of FeHx, FeS, FeSi and FeO in the core.
    """
    mFeHx = (1 - xiH) * mFe + xiH * mH
    x = np.array([1.0, -wt[0] * mFeHx, -wt[1] * mFeHx, -wt[2] * mFeHx])

    m = matrix(wt, xiH=xiH)

    a = np.linalg.solve(m, x)

    return a


def mat2at_core(xi=[1.0, 0.0, 0.0, 0.0], xiH=0.0):
    """Takes the material fractions (FeHx, FeS, FeSi, FeO) and converts it to
    atomic fractions xiFe, xiH, xiS, xiSi, xiO
    """
    xi[0] = max(1.0 - (sum(xi) - xi[0]), 0.0)

    n = np.array(
        [xi[0] * (1.0 - xiH) + sum(xi) - xi[0], xi[0] * xiH, xi[1], xi[2], xi[3]]
    )

    return [n[i] / sum(n) for i in range(len(n))]


def at2wt_core(at):
    """ """
    m = [mFe, mH, mS, mSi, mO]
    m_tilde = sum([m[i] * at[i] for i in range(len(m))])
    return [at[i] * m[i] / m_tilde for i in range(len(m))]


def N_tot_core(wt=[1 / 3, 1 / 3, 1 / 3], xiH=0.0):
    """Compute moles of Fe, H, S, Si, O per tot mole."""
    xi = wt2mol(wt=wt, xiH=xiH)
    return np.array(
        [xi[0] * (1.0 - xiH) + sum(xi) - xi[0], xi[0] * xiH, xi[1], xi[2], xi[3]]
    )


def xi_tot_core(wt=[1 / 3, 1 / 3, 1 / 3], xiH=0.0):
    """Compute xi_Fe, xi_H, xi_S, xi_Si and xi_O in the core."""
    N_tot = N_tot_core(wt=wt, xiH=xiH)
    return [N_tot[i] / sum(N_tot) for i in range(len(N_tot))]


def X_tot_core(wt=[1 / 3, 1 / 3, 1 / 3], xiH=0.0):
    """Compute X_Fe, X_H, X_S, X_Si and X_O in the core."""
    xi_tot = xi_tot_core(wt=wt, xiH=xiH)
    m = [mFe, mH, mS, mSi, mO]
    m_tilde = sum([m[i] * xi_tot[i] for i in range(len(m))])
    return [xi_tot[i] * m[i] / m_tilde for i in range(len(m))]


def probe_mantle_comps(N=100):
    range_P_CS = [1e9, 5e11]
    range_x_FeS = [0.0, 1.0]
    range_x_FeSi = [0.0, 1.0]
    range_x_FeO = [0.0, 1.0]

    ranges = [[1e9, 5e11], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0]]

    data = np.empty([N, 6])

    inputs = np.empty([N, len(ranges) + 2])
    for i in range(N):
        for j in range(len(ranges)):
            p = random.random()

            if j == 0:
                diff = np.log10(ranges[j][1]) - np.log10(ranges[j][0])
                val = np.log10(ranges[j][0]) + p * diff
                val = 10 ** val

            else:
                diff = ranges[j][1] - ranges[j][0]
                val = ranges[j][0] + p * diff

            inputs[i][j] = val

        ocmf = [0.0, inputs[i][1], inputs[i][2], inputs[i][3]]
        comp = mantle_comp(inputs[i][0], ocmf=ocmf)

        data[i] = [
            comp[0],
            comp[1],
            inputs[i][0],
            inputs[i][1],
            inputs[i][2],
            inputs[i][3],
        ]

    return data


def compute_model(pres_core_seg):
    """Compute a single valid model."""
    valid_composition = False
    while not valid_composition:
        # Randomly sample core composition components on a log scale
        xiFeS = ftool.sample_log_uniform(1e-4, 5e-1)
        xiFeSi = ftool.sample_log_uniform(1e-4, 3e-1)
        xiFeO = ftool.sample_log_uniform(1e-4, 2e-1)

        xi_all_core = [0.0, xiFeS, xiFeSi, xiFeO]
        
        # Compute mantle composition from core composition using the partitioning model
        Fe_number_mantle, Si_number_mantle = calc_equilibrium_mantle_comp(pres_core_seg, xi_all_core)

        # Check if the composition is within the feasible range
        simmin = Si_number_mantle_min(Fe_number_mantle)
        simmax = Si_number_mantle_max(Fe_number_mantle)
        femmin = 0.0
        femmax = 0.5

        if simmin <= Si_number_mantle <= simmax and femmin <= Fe_number_mantle <= femmax:
            valid_composition = True
            # return (0., .4, .0, .0, .0)
            return (Fe_number_mantle, Si_number_mantle, xiFeS, xiFeSi, xiFeO)


def calc_equilibrium_mantle_comp(P_CS, ocmf):
    """
    Computes the mantle composition according to the single
    stage core-segregation model.

    Parameters:
    P_CS (float): Core segregation pressure in Pa.
    ocmf (list): Outer core mass fractions.

    Returns:
    tuple (real): Molar abundance of Fe and Si in the silicates.
    """
    # Convert to atomic abundances
    xi = mat2at_core(ocmf, xiH=0.0)
    # Compute the core-segregation temperature
    T_CS = temp_liquidus_pyrolite(P_CS)

    # Compute molar abundances of Fe and Si
    fem = Fe_number_mantle(P_CS, T_CS, xi=xi)
    sim = Si_number_mantle(P_CS, T_CS, xi=xi)

    return fem, sim


# def plot_core_content(xiH=np.linspace(0.0, 0.5)):
#     y = np.empty([len(xiH), 5])
#     labels = ["Fe", "H", "S", "Si", "O"]
#     for i in range(len(y)):
#         bla = xi_tot_core(wt=[0.02, 0.06, 0.025], xiH=xiH[i])
#         for j in range(len(bla)):
#             y[i][j] = bla[j]

#     fig, ax = plt.subplots()
#     ax.set_xlabel("H concentration in iron hydride")
#     ax.set_ylabel("total element concentration in outer core (%)")
#     for i in range(len(y.T)):
#         ax.semilogy(xiH, y.T[i] * 100, label=labels[i])

#     ax.text(0.05, 1, "nominal case (Zhang et al. 2016):\n6 wt% Si, 2 wt% S, 2.5 wt% O")
#     ax.legend(loc=2)


def epsilon_ki(T, k, i):
    m = [mO * 1e-3, mSi * 1e-3]
    return eki[k][i] * m[i] / 0.242 * 1873.0 / T - m[i] / 55.85 + 1.0


def partition_coefficient_i(T, P, i, xi):
    """Compute metal-silicate partition coefficient according to
    Fischer et al. 2015 accounting for non-ideal effects in multi-component
    fluids. Currently only for O and Si. The effect of S on KD is not has not
    been investigated by these authors and no other sources were found.

    Paramters:
    T (float): Temperature in K.
    P (float): Pressure in Pa.
    i (int): Index of of species.
    xi (float): Molar concentrations.

    Returns:
    float: Partition coefficient of species i.
    """
    P *= 1e-9
    KD = a_KDi[i] + b_KDi[i] / T + c_KDi[i] * P / T
    eps = epsilon_ki(T, i, i)
    KD += eps * np.log(1.0 - xi[i]) / 2.303
    for k in range(2):
        if k == i:
            pass
        else:
            eps = epsilon_ki(T, k, i)
            delta = 1.0 / 2.303 * eps * xi[k]
            delta *= 1.0 + np.log(1.0 - xi[k]) / xi[k] - 1.0 / (1.0 - xi[i])
            KD += delta
    for k in range(2):
        if k == i:
            pass
        else:
            eps = epsilon_ki(T, k, i)
            delta = 1.0 / 2.303 * eps * xi[k] ** 2 * xi[i]
            delta *= (
                1.0 / (1 - xi[i])
                + 1.0 / (1.0 - xi[k])
                + xi[i] / (2.0 * (1.0 - xi[i]) ** 2)
                - 1.0
            )
            KD -= delta
    return 10 ** KD


def partition_coefficient(T, P, ll):
    """Compute metal-silicate partition coefficient according to
    Fischer et al. 2015. Currently only for O and Si.
    """
    P *= 1e-9
    return 10 ** (a_KD[ll] + b_KD[ll] / T + c_KD[ll] * P / T)


def KD_S(T, P, xi, which="suer"):
    """
    Partition coefficient between metals and silicates for S from
    Boujibar 2014 or Suer et al. 2017

    Parameters:
    T (float): Temperature in K.
    P (float): Pressure in Pa.
    which (str, optional): Model. Defaults to 'suer'.

    Returns:
    float: Partition coefficient for sulfur.
    """
    xiFe, xiH, xiS, xiSi, xiO = xi
    xiC = 0.0
    xiNi = 0.0
    P *= 1e-9

    xiFeO = xi_FeO(P, T, xi)
    xiSiO2 = xi_SiO2(P, T, xi)
    xiMgO = 1.0 - xiFeO - xiSiO2
    CS = 10 ** (-5.704 + 3.15 * xiFeO + 0.12 * xiMgO)

    if which == "bijou":
        b = 405.0
        c = 136.0
        d = 32.0
        e = 181.0
        f = 305.0
        g = 30.2
        h = 1.13
        i = 10.7
        j = 31.4
        k = -3.72

        KD = np.log10(xiFeO) - np.log10(CS) + b / T + c * P / T
        KD += d * np.log10(1.0 - xiSi) + e * (np.log10(1.0 - xiSi)) ** 2
        KD += f * (np.log10(1.0 - xiSi)) ** 3 + g * np.log10(1.0 - xiC)
        KD += h * np.log10(1.0 - xiFe) + i * np.log10(1.0 - xiNi)
        KD += j * np.log10(1.0 - xiO) + k

    elif which == "suer":
        KD = (
            -3.3
            + 3000 / T
            + 33 * P / T
            + np.log(xiFeO)
            - np.log(CS)
            + 14 * np.log(1.0 - xiO)
        )

    return 10 ** KD


def Margules_eq(P, T, A, B, C):
    """
    Implements the of the Margules equation.

    Parameters:
    P (float): Pressure in Pa.
    T (float): Temperature in K.
    A (float): First Margules parameter.
    B (flaot): Second Margules parameter.
    C (float): Third Margules parameter.

    Returns:
    float: Margules coefficient.
    """
    return A - B * T - C * P / 1e5


def W_Fe_FeO(P, T):
    """
    Interaction parameters for the activity coefficient of FeO from
    Frost et al. 2010. Includes smoothing from non-ideal to ideal regime from
    Schaefer et al. 2017.

    Parameters
    ----------
    P : FLOAT
        Pressure in Pa.
    T : FLOAT
        Temperature in K.

    Returns
    -------
    Float.

    """
    A = 83307.0
    B = 8.978
    C = 0.09
    return Margules_eq(P, T, A, B, C)


def W_FeO_Fe(P, T):
    """
    Interaction parameter for the activity coefficient of Fe from
    Frost et al. 2010. Includes smoothing from non-ideal to ideal regime from
    Schaefer et al. 2017.
    """
    A = 135943.0
    B = 31.122
    C = 0.059
    return Margules_eq(P, T, A, B, C)


def W_Fe_FeO_prime(P, T, T0, P0, a, b):
    A = 83307.0
    B = 8.978
    C = 0.09
    return -B * T_liquidus_pyrolite_prime(P) - C


def W_FeO_Fe_prime(P, T, T0, P0, a, b):
    A = 135943.0
    B = 31.122
    C = 0.059
    return -B * T_liquidus_pyrolite_prime(P) - C


def coefs_Fe_FeO(P, xiFe):
    T = temp_liquidus_pyrolite(P)
    T_trans = temp_liquidus_pyrolite(P_FeO_Fe_trans)

    W1 = W_FeO_Fe(P_FeO_Fe_trans, T_trans)
    W2 = W_Fe_FeO(P_FeO_Fe_trans, T_trans)
    dW1 = W_FeO_Fe_prime(P_FeO_Fe_trans, T_trans, 1940, 0.0, 29e9, 1.0 / 1.9)
    dW2 = W_Fe_FeO_prime(P_FeO_Fe_trans, T_trans, 1940, 0.0, 29e9, 1.0 / 1.9)

    K = np.exp((1 - xiFe) ** 2 * (W2 + 2.0 * (W1 - W2) * xiFe) / (Rgas * T_trans))
    K -= 1.0
    T_prime_trans = T_liquidus_pyrolite_prime(P_FeO_Fe_trans)
    g_prime = (
        1.0 / (Rgas * T_trans) * (1.0 - xiFe) ** 2 * (dW2 + 2.0 * (dW1 - dW2) * xiFe)
    )
    g_prime += (
        -1.0
        / (Rgas * T_trans ** 2)
        * T_prime_trans
        * (1.0 - xiFe) ** 2
        * (W2 + 2.0 * (W1 - W2) * xiFe)
    )
    g_prime *= np.exp(
        (1.0 - xiFe) ** 2 * (W2 + 2.0 * (W1 - W2) * xiFe) / (Rgas * T_trans)
    )
    g_prime = ftool.deriv(
        f=gamma_Fe, x0=P_FeO_Fe_trans, whicharg="P", xiFe=xiFe, acc=1e-3
    )
    Z = -g_prime / K
    return K, Z


def coefs_FeO_Fe(P, xiFeO):
    T = temp_liquidus_pyrolite(P)
    T_trans = temp_liquidus_pyrolite(P_FeO_Fe_trans)

    W1 = W_FeO_Fe(P_FeO_Fe_trans, T_trans)
    W2 = W_Fe_FeO(P_FeO_Fe_trans, T_trans)
    dW1 = W_FeO_Fe_prime(P_FeO_Fe_trans, T_trans, 1940, 0.0, 29e9, 1.0 / 1.9)
    dW2 = W_Fe_FeO_prime(P_FeO_Fe_trans, T_trans, 1940, 0.0, 29e9, 1.0 / 1.9)

    K = np.exp((1 - xiFeO) ** 2 * (W1 + 2.0 * (W2 - W1) * xiFeO) / (Rgas * T_trans))
    K -= 1.0
    T_prime_trans = T_liquidus_pyrolite_prime(P_FeO_Fe_trans)
    g_prime = (
        1.0 / (Rgas * T_trans) * (1.0 - xiFeO) ** 2 * (dW1 + 2.0 * (dW2 - dW1) * xiFeO)
    )
    g_prime += (
        -1.0
        / (Rgas * T_trans ** 2)
        * T_prime_trans
        * (1.0 - xiFeO) ** 2
        * (W1 + 2.0 * (W2 - W1) * xiFeO)
    )
    g_prime *= np.exp(
        (1.0 - xiFeO) ** 2 * (W1 + 2.0 * (W2 - W1) * xiFeO) / (Rgas * T_trans)
    )
    g_prime = ftool.deriv(
        f=gamma_FeO, x0=P_FeO_Fe_trans, whicharg="P", xiFeO=xiFeO, acc=1e-3
    )
    Z = -g_prime / K
    return K, Z


def W_FeO_MgO(P):
    return 11e3 + 0.011 * P / 1e5


def T_liquidus_pyrolite_prime(P):
    # Andrault 2011
    T0 = 1940
    a = 29e9
    c = 1.9

    return T0 * 1.0 / c / a * (1.0 + P / a) ** (1.0 / c - 1.0)


def gamma_FeO(P, x_FeO=0.0):
    """Interaction parameter of FeO from Frost et al. 2010.

    Parameters:
    P (float): Pressure in Pa.
    x_FeO (float, optional): Mole fraction of FeO. Defaults to 0.

    Returns:
    float: Interaction parameter.
    """
    T = temp_liquidus_pyrolite(P)
    W1 = W_FeO_Fe(P, T)
    W2 = W_Fe_FeO(P, T)
    r = (1.0 - x_FeO) ** 2 * (W1 + 2.0 * (W2 - W1) * x_FeO)
    r /= Rgas * T
    return np.exp(r)


def gamma_Fe(P, x_Fe=None):
    """Interaction parameter of Fe from Frost et al. 2010.

    Parameters:
    P (float): Pressure in Pa.
    x_Fe (float, optional): Mole fraction of Fe. Defaults to 0.

    Returns:
    float: Interaction parameter.
    """
    T = temp_liquidus_pyrolite(P)
    W1 = W_FeO_Fe(P, T)
    W2 = W_Fe_FeO(P, T)
    r = (1.0 - x_Fe) ** 2 * (W2 + 2.0 * (W1 - W2) * x_Fe)
    r /= Rgas * T
    return np.exp(r)


def gamma_FeO_smoothed(P, xiFeO):
    xiFeO = min(xiFeO, 0.99999)
    if P < P_FeO_Fe_trans:
        return gamma_FeO(P=P, xiFeO=xiFeO)

    else:
        K, Z = coefs_FeO_Fe(P, xiFeO)
        return max(1.0 + K * np.exp(-Z * (P - P_FeO_Fe_trans)), 1.0)


def gamma_Fe_smoothed(P, xiFe):
    xiFe = min(xiFe, 0.99999)
    if P < P_FeO_Fe_trans:
        return gamma_Fe(P=P, xiFe=xiFe)

    else:
        K, Z = coefs_Fe_FeO(P, xiFe)
        return max(1.0 + K * np.exp(-Z * (P - P_FeO_Fe_trans)), 1.0)


# def plot_activity_coefficients():
#     fig, ax = plt.subplots(figsize=(4, 3))
#     # ax.set_yscale('log')
#     axin = ax.inset_axes([0.7, 0.2, 0.025, 0.4])
#     ax.tick_params(right=True, top=True, direction="in")
#     ax.set_xlabel(r"Core Segregation Pressure [GPa]")
#     ax.set_ylabel(r"Activity Coefficient")
#     ax.set_xlim(0, 80)
#     ax.set_ylim(0, 10)
#     x = np.linspace(1e9, 100e9)
#     fracs = np.linspace(1.0, 0.1, len(color_list))
#     cmap = ftool.my_cmap()
#     cbar = mpl.colorbar.ColorbarBase(axin, cmap=cmap, ticks=np.arange(0, 1.2, 0.2))

#     cbar.set_label(r"$X_{\rm Fe}^{\rm Metal}$ or $X_{\rm FeO}^{\rm Silicates}$")
#     cbar_ticks = np.linspace(0.0, 1.0, 6)
#     cbar.ax.set_yticklabels(np.round(cbar_ticks, 1))

#     plot_list = []
#     label_list = [r"$\gamma_{\rm FeO}$", r"$\gamma_{\rm Fe}$"]

#     for f in range(len(fracs)):
#         ff = fracs[f]
#         y1 = np.array([gamma_FeO_smoothed(xx, ff) for xx in x])
#         y2 = np.array([gamma_Fe_smoothed(xx, ff) for xx in x])

#         (pl1,) = ax.plot(x * 1e-9, y1, linestyle="-", color=color_list[f])
#         (pl2,) = ax.plot(x * 1e-9, y2, linestyle="--", color=color_list[f])
#         if f == len(fracs) - 1:
#             plot_list.append(pl1)
#             plot_list.append(pl2)

#     legend = ax.legend(plot_list, label_list)
#     ax.add_artist(legend)
#     fig.savefig(
#         "/home/os18o068/Documents/PHD/Abbildungen/activity_coeffs.pdf",
#         format="pdf",
#         bbox_inches="tight",
#     )

#     plt.close("all")


def xi_S(P, T, xi):
    """
    Computes mol fraction of sulfur in the mantle assuming chemical
    equilibrium between mantle and core. P, T at CMB and xiFe and xiO in core.

    Parameters
    ----------
    P (float): Pressure in Pa.
    T (float): Temperature in K.
    xi (list): Molar abundances in the core.

    Returns
    -------
    float: Molar abundance of S in the silicates.
    """
    KD = KD_S(T, P, xi)
    return xi[2] / KD


def xi_FeO(P, T, xi):
    """
    Computes mol fraction of iron oxide in the mantle assuming chemical
    equilibrium between mantle and core. P, T at CMB and xiFe and xiO in core.

    Parameters
    ----------
    P (float): Pressure in Pa.
    T (float): Temperature in K.
    xi (list): Molar abundances in the core.

    Returns
    -------
    float: Molar abundance of FeO in the silicates.
    """
    xiFe, xiH, xiS, xiSi, xiO = xi
    KD = partition_coefficient_i(T, P, 1, [xi[3], xi[4]])
    return xiFe * xiO / KD


def xi_SiO2(P, T, xi):
    """
    Computes mol fraction of SiO2 in the mantle assuming chemical
    equilibrium between mantle and core. P, T at CMB and xiFe, xiSi and xiO
    in core.

    Parameters
    ----------
    P (float): Pressure in Pa.
    T (float): Temperature in K.
    xi (list): Molar abundances in the core.

    Returns
    -------
    float: Molar abundance of SiO2 in the silicates.
    """
    xi[0] = 1.0 - (sum(xi) - xi[0])
    xiFe, xiH, xiS, xiSi, xiO = xi
    xiFeO = xi_FeO(P, T, xi)
    KD_Si = partition_coefficient_i(T, P, 0, [xi[3], xi[4]])
    return xiSi * xiFeO / (xiFe * KD_Si)


def logfO2(P, xiFe, xiFeO):
    """
    Computes oxygen fugacity according to Rose-Weston et al. 2009.
    The activity coefficients for Fe in the metal phase and FeO in the silicate
    phase are computed using a similar smoothing as in Schaefer et al. 2017 and
    along the pyrolite liquidus curve from Andrault 2011.
    """
    gamma_Fe_ = gamma_Fe_smoothed(P, xiFe)
    gamma_FeO_ = gamma_FeO_smoothed(P, xiFeO)
    aFe = gamma_Fe_ * xiFe
    aFeO = gamma_FeO_ * xiFeO
    return 2 * np.log10(aFeO / aFe)


def Fe_number_mantle(P, T, xi):
    """
    Computes Fe# in the mantle assuming chemical equilibrium between mantle
    and core. P, T at CMB and xi = xiFe, xiH, xiS, xiSi, xiO in core.

    Parameters:
    P (float): Pressure in Pa.
    T (float): Temperature in K.
    xi (float): Molar abundances of the core.

    Returns:
    float: Iron number in the silicates.
    """
    xiFe, xiH, xiS, xiSi, xiO = xi
    xiSiO2 = xi_SiO2(P, T, xi)
    xiFeO = xi_FeO(P, T, xi)
    result = xiFeO / (1.0 - xiSiO2)
    # print ('P, T, xi =', P, T, xi)
    # print ('xiSiO2 =', xiSiO2)
    # print ('xiFeO =', xiFeO)
    if result <= 0.0 or result > xi_Fe_mantle_max:
        result = xi_Fe_mantle_max
    return result

def Si_number_mantle_max(xiFe):
    return 1. / (2. - xiFe)

def Si_number_mantle_min(xiFe):
    return 1. / (3. - 2. * xiFe)

def Si_number_mantle(P, T, xi):
    """
    Computes Si# in the mantle assuming chemical equilibrium between mantle
    and core. P, T at CMB and xi = xiFe, xiH, xiS, xiSi, xiO in core.

    Parameters
    ----------
    P (float): Pressure in Pa.
    T (float): Temperature in K.
    xi (float): Molar abundances of the core.

    Returns
    -------
    float: Silicon number in the silicates.
    """
    xiFe, xiH, xiS, xiSi, xiO = xi
    xiSiO2 = xi_SiO2(P, T, xi)
    xiFeO = xi_FeO(P, T, xi)
    SiMg = xiSiO2 / (1 - xiFeO - xiSiO2)
    result = SiMg / (1 + SiMg)
    # print ('P, T, xi =', P, T, xi)
    # print ('xiSiO2 =', xiSiO2)
    # print ('xiFeO =', xiFeO)
    # print ('Si/Mg =', SiMg)
    # result = min(result, Si_number_max(1-xiFeO))
    # result = max(result, Si_number_min(1-xiFeO))

    return result


def xi_Fe_mantle_min(MgSi):
    """
    Compute the min. Fe content in the silicates for given Mg/Si ratio.

    Returns
    -------
    Float.

    """

    # Calculation performed for (Mg,Fe)2SiO4 because for pyroxene Mg/Si
    return 1.0 - MgSi / 2.0


def xi_mantle(T, P, ll, x_core=0.0, x_Fe_core=0.0, x_O_core=0.0):
    """
    Computes the composition of the silicates from the core composition
    according to the single stage core-segregation model.

    Parameters:
    T (float): Temperature in K.
    P (float): Pressure in Pa.
    x_core (float):
    x_Fe_core (float): Molar Fe concentration in metals.
    x_O_core (float): Molar O concentration in metals.

    Returns:
    tuple: Molar abundance of oxygen and iron in the silicates.
    """
    KD = partition_coefficient(T, P, ll)

    # # Oxygen
    # if ll == 1:
    #     return xi_core / KD

    # else:

    #     # Compute FeO content in mantle first
    #     KD_FeO = partition_coefficient(T, P, 1)
    #     xi_FeO_mantle = xi_Fe_core * xi_O_core / KD_FeO
    #     # print("log KD_FeO =", np.log10(KD_FeO))
    #     # print("xi_FeO_mantle =", xi_FeO_mantle)
    #     return xi_core / xi_Fe_core * xi_FeO_mantle / KD

    # Compute FeO content in mantle first
    KD_FeO = partition_coefficient(T, P, 1)
    xi_FeO_mantle = x_Fe_core * x_O_core / KD_FeO
    return x_core / KD, x_core / x_Fe_core * xi_FeO_mantle / KD


def T_melt_MgSiO3(P):
    # Belonoshko et al. 2005
    a = 4.6e9
    b = 0.33
    T0 = 1831.0
    P0 = 0.0

    return T0 * (1.0 + (P - P0) / a) ** b


def T_melt_CaSiO3(P):
    # Braithwaite 2019
    a = 48.8e9
    b = 0.413
    c = 860e9
    T0 = 4020
    P0 = 44.2e9

    return T0 * (1.0 + (P - P0) / a) ** b * np.exp(-(P - P0) / c)


def P_CS(M, a=1.5, P0=40e9):
    """
    Estimate pressure of core segregation using a simple scaling law.
    """
    return P0 * M ** a


# def xSievert(
#     P=1e5,
#     T=300,
#     P0=1e5,
#     mSolv=2 * mH,
#     mSubs=mMg + mSi + 3 * mO,
#     x=0.1,
#     rhoBulk=3e3,
#     rhoSubs=4e3,
#     llSubs=1,
#     deltaH=-31.8,
#     deltaS=+38.1,
# ):
#     # Compute wt fraction of solvent
#     mTilde = x * mSolv + (1.0 - x) * mSubs
#     w = x * mSolv / mTilde

#     # Compute density of pure solvent
#     rhoSolv = w / (1.0 / rhoBulk - (1.0 - w) / rhoSubs)  # P * mSolv / (NA * kB * T)

#     # print ('rhoSolv =', rhoSolv)
#     # Use ideal gas to compute partial pressure of solvent in substrate
#     partialP = rhoSolv / mSolv * Rgas * T
#     # print ('partial pressure IGL (MPa) =', partialP * 1e-6)
#     # Use van der waasl EoS to compute partial pressure of solvent in substrate
#     partialP = (
#         rhoSolv * Rgas * T / (mSolv - rhoSolv * 26.61e-6)
#         - rhoSolv**2 * 24.76e-3 / (mSolv) ** 2
#     )

#     # print ('partial pressure VDW (MPa) =', partialP * 1e-6)

#     return (partialP / P0) ** (1 / 2) * np.exp((deltaH - T * deltaS) / (Rgas * T))


# def plotSievert(res=3, xlims=[1e-3, 1e-1], ylims=[0, 1]):
#     fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
#     bulkDensities = [2000, 3000]
#     subsDensities = [4000, 5000]
#     temps = np.linspace(1000, 5000, 5)
#     moleFractions = np.logspace(-3, -1, 2**res)
#     cols = ["r", "g", "b", "k", "gray"]

#     data = np.empty([len(bulkDensities), len(subsDensities), len(temps), 2**res])
#     for i in range(len(bulkDensities)):
#         for j in range(len(subsDensities)):
#             for k in range(len(temps)):
#                 data[i][j][k][:] = xSievert(
#                     rhoBulk=bulkDensities[i],
#                     rhoSubs=subsDensities[j],
#                     T=temps[k],
#                     x=moleFractions,
#                 )

#                 ax[i][j].semilogx(moleFractions, data[i][j][k], color=cols[k])

#     for i in range(len(ax)):
#         for j in range(len(ax[i])):
#             ax[i][j].set_xlim(xlims)
#             ax[i][j].set_ylim(ylims)
#             ax[i][j].tick_params(top=True, right=True, which="both")
#             trafo = transforms.blended_transform_factory(
#                 ax[i][j].transAxes, ax[i][j].transAxes
#             )

#             d = r"$\rho_{\rm bulk}$"
#             a = r"${}\ \rm kg / m^3$".format(str(bulkDensities[i]))
#             ax[i][j].text(0.1, 0.9, f"{d} ={a}", transform=trafo)
#             d = r"$\rho_{\rm subs}$"
#             a = r"${} \ \rm kg / m^3$".format(str(subsDensities[j]))
#             ax[i][j].text(0.1, 0.8, f"{d} ={a}", transform=trafo)

#     for i in range(len(ax)):
#         ax[i][0].set_ylabel(r"$\rm H_2 \ mole \ fraction \ in \ metal$")

#     for i in range(len(ax)):
#         ax[1][i].set_xlabel(r"$\rm H_2 \ mole \ fraction \ in \ substrate$")

#     lines = ax[0][0].lines
#     labels = [r"${} \ \rm K$".format(int(t)) for t in temps]
#     ax[0][0].legend(lines, labels, loc=3)

#     fig.savefig(plotPath + "siverts_law.pdf", format="pdf", bbox_inches="tight")
#     plt.close(fig)


# def plot_logfO2():
#     xFeO = np.logspace(-3, -1)
#     xFe = 0.9

#     pres = [1e9, 10e9, 1e11]
#     fig, ax = plt.subplots()
#     for i in range(len(pres)):
#         y = []
#         for j in range(len(xFeO)):
#             y.append(logfO2(pres[i], xFe, xFeO[j]))

#         ax.semilogx(xFeO, y)

#     fig.savefig(plotPath + "oxygen_fug.pdf", format="pdf", bbox_inches="tight")
#     plt.close(fig)


def temp_melt_iron(P, X_Si, X_O, X_S):
    """
    Computes melting temperature of iron alloys according
    to Li et al. 2020. The effect of O, Si, and S are accounted
    for according to Andrault et al. 2016.

    Parameters:
    P (float): Pressure in Pa.
    X_Si (float): Molar concentration of silicon.
    X_S (float): Molar concentration of sulfur.
    X_O (float): Molar concentration of oxygen.

    Returns:
    float: melting temperature in K.
    """
    # Li et al. 2020, fit for static + present shock experiments  between
    # 50 and 256 GPs (see their page 7)
    T = 1811.0 * ((P - 1.0e5) / 23e9 + 1.0) ** (1.0 / 2.26)

    # Account for impurities (Andrault et al. 2016)
    T -= 3e3 * X_Si + 5e3 * X_O + 1e4 * X_S
    return T


def T_melt_Fe_new(P):
    # Stixrude 2014
    return 6500 * (P / 340e9) ** 0.515


def temp_solidus_pyrolite(P):
    """
    Compute solidus temperature of a pyrolite composition
    according to Andrault et al. 2016.

    Parameters:
    P (float): Pressure in Pa.

    Returns:
    float: Solidus temperature in K.
    """
    # Andrault 2011
    T0 = 2045
    a = 92e9
    c = 1.3

    return T0 * (1.0 + P / a) ** (1.0 / c)


def temp_liquidus_pyrolite(P):
    """
    Compute liquidus temperature of a pyrolite composition
    according to Andrault et al. 2016.

    Parameters:
    P (float): Pressure in Pa.

    Returns:
    float: Liquidus temperature in K.
    """
    # Andrault 2011
    T0 = 1940
    a = 29e9
    c = 1.9

    return T0 * (1.0 + P / a) ** (1.0 / c)


def taylorN_Mg(X_H2O):

    x = 1.0 / xi_H2O_Ol(X_H2O)

    print("x =", x)

    a1 = -2.0
    a2 = -(mOl - mH2O)
    b1 = 2.0
    b2 = mOl

    k1 = (a1 + b1 * x) * (a2 + b2 * x) ** (-1)
    k2 = b1 * (a2 + b2 * x) ** (-1) - (a1 + b1 * x) * (a2 + b2 * x) ** (-2) * b2
    k3 = -b1 * (a2 + b2 * x) ** (-2) * b2 - (
        b1 * (a2 + b2 * x) ** (-2) * b2
        + (a1 + b1 * x) * (-2) * (a2 + b2 * x) ** (-3) * b2 ** 2
    )

    k2 *= x
    k3 *= 0.5 * x ** 2

    print(k1, k2, k3)

    return k1 + k2 + k3


def xi(eta, m1, m2):
    """Compute mole fraction from mass fraction of species 2 where species
    1 has a molar abundance of (1-xi). eta is between 0.0 and 1.0
    """
    return m1 * eta / (eta * m1 - eta * m2 + m2)


def eta(xi, m1, m2):
    """Compute mass fraction from mole fraction of species 2 where species
    1 has a weight abundance of (1-eta). xi is between 0.0 and 1.0
    """
    return xi * m2 / ((1.0 - xi) * m1 + xi * m2)


def compute_oxide_fractions(Si_number, x_Fe):
    """Computes oxide fractions of MgO, SiO2, FeO from Si# = [Si] / [Mg + Si] and
    the iron number xi_Fe = [Fe] / [Mg + Fe] in the mantle.
    """
    xiFeO = (1.0 - Si_number) / ((1.0 - x_Fe) / x_Fe + 1.0 - Si_number)
    xiSiO2 = Si_number * (1.0 - xiFeO)
    xiMgO = 1.0 - xiFeO - xiSiO2
    return xiMgO, xiSiO2, xiFeO


def silicon_number_max(x_Fe):
    """Computes max Si# that is allowed at given Mg# for pure per + ol
    composition
    """
    return 1.0 / (2.0 - x_Fe)


def silicon_number_min(x_Fe):
    """Computes min Si# that is allowed at given Mg# for pure per + ol
    composition
    """
    return 1.0 / (3.0 - 2.0 * x_Fe)


def Si2Mg_UM(xiOl=1.0, xiPyr=0.0, xiStv=0.0, xiFe=0.0):

    if not xiOl + xiPyr + xiStv == 1.0:
        return 0.0

    else:
        return (2.0 * xiPyr + xiOl + xiStv) / (2.0 * (xiPyr - 2.0 * xiFe + xiOl))


def Si2Mg(Mg_number=Mg_number_solar, Si_number=Si_number_solar):
    """Computes ratio Mg/Si for given Mg# and Si#. Note that for a pure
    per + ol mantle Mg/Si <= 0.5
    """
    return (1.0 - Mg_number) / (1.0 - Si_number) * Si_number / Mg_number


def xi_Stv_bounds(xi_Fe=0.0, Si_number=0.0):
    SiMg = Si_number / (1.0 - Si_number)
    # Lower mantle
    xi1 = (SiMg - 1.0 / (1.0 - xi_Fe)) / SiMg
    xi2 = SiMg * (1.0 - xi_Fe) / (SiMg * (1.0 - xi_Fe) + 1.0)

    # Upper mantle
    xi3 = 2.0 * (1.0 - SiMg * (1.0 - xi_Fe)) / (1.0 - 2.0 * SiMg * (1.0 - xi_Fe))
    xi4 = (2.0 * SiMg * (1.0 - xi_Fe) - 1.0) / (2.0 * SiMg * (1.0 - xi_Fe))

    xi1 = max(xi1, 0.0)
    xi2 = max(xi2, 0.0)
    xi3 = max(xi3, 0.0)
    xi4 = max(xi4, 0.0)

    xi1 = min(xi1, 1.0)
    xi2 = min(xi2, 1.0)
    xi3 = min(xi3, 1.0)
    xi4 = min(xi4, 1.0)

    x1 = max(xi1, xi2)
    x2 = max(xi3, xi4)

    x3 = min(xi1, xi2)
    x4 = min(xi3, xi4)

    print(xi1, xi2, xi3, xi4)
    return max(xi3, x4), min(x1, x2)


def Fe2Mg_max(SiMg, lay=None):
    """Compute maximum FeMg ratio allowed for given SiMg ratio in lower or
    upper mantle.

    Parameters:
    SiMg (float): Si to Mg ratio.
    lay (int, optional): Layer. Defaults to None.

    Returns:
    float: Fe to Mg ratio.
    """
    # upper mantle
    if lay == 2:
        # no upper limit
        return 1.0e10

    # lower mantle
    elif lay == 3:
        return np.maximum(-1.0 + 2.0 * SiMg, 0.0)

    else:
        return 10.0


def Fe2Mg_min(SiMg, lay=None):
    """Compute minimum FeMg ratio allowed for given SiMg ratio in lower or
    upper mantle.

    Parameters:
    SiMg (float): Si to Mg ratio.
    lay (int, optional): Layer. Defaults to None.

    Returns:
    float: Fe to Mg ratio.
    """
    # lower mantle
    if lay == 2:
        return np.maximum(-1.0 + SiMg, 0.0)

    # upper mantle
    elif lay == 3:
        return np.maximum(-1.0 + 2.0 * (SiMg - 1.0), 0.0)

    else:
        return 0.0


def silicon_number(SiMg, Mg_number):
    """Computes Si# from Si/Mg ratio at given Mg#. Note that this calculation
    is independant on the mineral composition at hand but is simply dictated
    by the given molar ratios for Si, Mg and Fe.

    Parameters:
    SiMg (float): Si to Mg ratio.
    Mg_number (float): Magnesium number.
    """
    if SiMg > 0.0:
        return 1.0 / (1.0 + 1.0 / SiMg * (1.0 / Mg_number - 1))

    else:
        return 0.0


def xi_Ws(SiMg=None, FeMg=None, xi_H2O_Ws=0.0, lay=1):
    """Computes mole fraction of Wuestite at given ratios Si/Mg and Fe/Mg
    for hydration model type 1. The hydrated phase is Brucite. The sample
    consists of MgO + FeO and H2O if MgO is hydrated
    """
    # check consistency if FeMg and SiMg in given mantel
    if FeMg < Fe2Mg_min(SiMg, lay=lay) or FeMg > Fe2Mg_max(SiMg, lay=lay):
        print("WARNING: given Fe/Mg out of range!")
        print(
            "Fe/Mg must be in the interval",
            Fe2Mg_min(SiMg, lay=lay),
            Fe2Mg_max(SiMg, lay=lay),
        )

        return None

    # lower mantle
    if lay == 2:
        xi_Fe = FeMg / (1 + FeMg)
        return (SiMg * (1 - xi_Fe) - 1) / (
            SiMg * (1 - xi_Fe) * xi_H2O_Ws - xi_H2O_Ws - 1
        )

    # upper mantle
    # no Wuestite in upper mantle
    elif lay == 3:
        return 0.0


def xi_Br(SiMg=None, FeMg=None, lay=1):
    """Computes mole fraction of periclase at given ratios Si/Mg and Fe/Mg
    for hydration model type 1
    """
    # lower mantle
    if lay == 2:
        return max((1.0 - 2 * SiMg + FeMg) / (1.0 - SiMg + FeMg), 0.0)

    # upper mantle
    elif lay == 3:
        return 0.0


def xi_Ol(SiMg=None, FeMg=None, xi_H2O_Ol=0.0, lay=1):
    """Computes mole fraction of olivine at given ratios Si/Mg and Fe/Mg
    for hydration model type 1
    """
    # check consistency if FeMg and SiMg in given mantel
    if FeMg < Fe2Mg_min(SiMg, lay=lay) or FeMg > Fe2Mg_max(SiMg, lay=lay):
        print("WARNING: given Fe/Mg out of range!")
        print(
            "Fe/Mg must be in the interval",
            Fe2Mg_min(SiMg, lay=lay),
            Fe2Mg_max(SiMg, lay=lay),
        )
        print("given: ", FeMg)

        return None

    else:
        # no Olivine in lower mantle
        if lay < 3:
            return 0.0

        # upper mantle
        elif lay == 3:
            xi_Fe = FeMg / (1 + FeMg)
            return (
                2
                * (SiMg * (1 - xi_Fe) - 1)
                / (2 * SiMg * (1.0 - xi_Fe) * xi_H2O_Ol - xi_H2O_Ol - 1.0)
            )


def xi_Perov(SiMg=None, FeMg=None, xi_H2O_Ws=0.0, lay=1):
    """Compute mole fraction of Perovskite for given values of Si/Mg and Fe/Mg"""
    # check consistency if FeMg and SiMg in given mantel
    if FeMg < Fe2Mg_min(SiMg, lay=lay) or FeMg > Fe2Mg_max(SiMg, lay=lay):
        print("WARNING: given Fe/Mg out of range!")
        print(
            "Fe/Mg must be in the interval",
            Fe2Mg_min(SiMg, lay=lay),
            Fe2Mg_max(SiMg, lay=lay),
        )

        return None

    # lower mantle
    if lay == 2:
        xi_Fe = FeMg / (1 + FeMg)
        return 1.0 - (SiMg * (1 - xi_Fe) - 1) / (
            SiMg * (1 - xi_Fe) * xi_H2O_Ws - xi_H2O_Ws - 1
        )

    # def plot_abundance_change(SiMg=None, FeMg=None, lay=1):
    #     """Visualize how the relative abundances xi_Ol vs. xi_En changes as a
    #     function of the hydration level. This gives the range within which the
    #     abundances have to be updated in each shell.
    #     """

    #     fig, ax = plt.subplots()

    #     # Create range of hydration in mol% (not physical!!!)
    #     xiH2O = np.logspace(-3, -1)
    #     FeMg_list = np.linspace(0.0, 0.5, 6)

    #     for FeMg in FeMg_list:
    #         xiOl_dry = xi_Ol(SiMg=SiMg, FeMg=FeMg, xi_H2O_Ol=0.0, lay=lay)
    #         xiFe = xi_Fe(FeMg=FeMg, SiMg=SiMg)
    #         print(xiFe)
    #         SiMg_list = (2.0 - xiOl_dry * (1.0 + xiH2O)) / (
    #             2 * (1 - xiFe) * (1.0 - xiOl_dry * xiH2O)
    #         )

    #         xiOl = xi_Ol(SiMg=SiMg, FeMg=FeMg, xi_H2O_Ol=xiH2O, lay=lay)

    #         ax.semilogy(xiH2O, (SiMg_list - SiMg) / SiMg)

    # def plot_molarmass(SiMg=[], xmin=0.0, xmax=0.2):
    #     """ """
    #     fig, ax = plt.subplots()
    #     ax.set_xlim(xmin * 100, xmax * 100)

    #     ax.set_xlabel(r"$X_{H_2 O} \ in  \ Olivine \ [wt \%]$")
    #     ax.set_ylabel(r"$\rm molar \ mass \ [kg]$")

    #     substances = [mH2O, mBr, mPer, mOl]
    #     substances_names = [r"$H_2 O$", r"$Mg(OH)_2$", r"$MgO$", r"$Mg_2 Si O_4$"]

    #     for i in range(len(substances)):
    #         sub = substances[i]
    #         name = substances_names[i]
    #         ax.plot([xmin * 100, xmax * 100], [sub, sub], color="k", linestyle=":")
    #         ax.text(5.0, sub * 1.01, name)

    #     x = np.linspace(xmin, xmax, 100)

    #     for SM in SiMg:
    #         y = N_tot(M=1.0, SiMg=SM, ph_per=2, ph_ol=0, X_H2O_ol=x, lay=2)

    #         ax.plot(x * 100, 1 / y, label="Si/Mg = " + str(round(SM, 3)))

    #     ax.legend()

    # def plot_abundance(MgSi=[]):
    #     """ """
    #     fig, ax = plt.subplots()
    #     ax.set_xlabel(r"$Mg \#$")
    #     ax.set_ylabel(r"$Si \#$")

    #     x = np.linspace(0.0, 1.0)
    #     y = []

    #     for MS in range(len(MgSi)):
    #         y.append(1.0 / (1.0 + 1.0 / SiMg[MS] * (1.0 / x - 1.0)))

    #         ax.plot(x, y[MS], label="Mg/Si =" + str(MgSi[MS]))

    #     ax.legend(frameon=False)
    # upper mantle
    # No Perovskite in upper mantle
    elif lay == 3:
        return 0.0


def xi_Fe(SiMg=None, FeMg=0.0, lay=1):
    """Compute mole fraction of Fe in the mantle region for given Si/Mg and
    Fe/Mg ratios
    """
    # check consistency if FeMg and SiMg in given mantel
    if FeMg < Fe2Mg_min(SiMg, lay=lay) or FeMg > Fe2Mg_max(SiMg, lay=lay):
        print("WARNING: given Fe/Mg out of range!")
        print(
            "Fe/Mg must be in the interval",
            Fe2Mg_min(SiMg, lay=lay),
            Fe2Mg_max(SiMg, lay=lay),
        )

        return None

    # lower mantle
    if lay == 2:
        return FeMg / (1 + FeMg)

    # upper mantle
    elif lay == 3:
        return FeMg / (1 + FeMg)


def xi_H2O_Ol(X_H2O_Ol=0.0, FeMg=0.0, lay=1):
    """Computes mole fraction of H2O in Olivine given a value for the weight
    fraction X_H2O (NOT in %)
    """
    xi_Fe = FeMg / (1 + FeMg)
    mOl_prime = mOl * (1.0 - xi_Fe) + xi_Fe * (mOl - 2 * mMg + 2 * mFe)

    # No Olivine in core and lower mantle
    if lay == 2 or lay == 0 or lay == 1:
        return 0.0

    elif lay == 3:
        return xi(eta=X_H2O_Ol, m1=mOl_prime, m2=mH2O)


def eta_H2O_Ws(xi_H2O_Per=0.0, FeMg=0.0):
    """Computes the weight fraction of H2O in Wuestite given a value for the
    mole fraction X_H2O (NOT in %) of H2O in Periclase
    """
    xi_Fe = FeMg / (1.0 + FeMg)
    e = (
        (1.0 - xi_Fe)
        * xi_H2O_Per
        * mH2O
        / (
            (1.0 - xi_Fe) * ((1.0 - xi_H2O_Per) * mPer + xi_H2O_Per * mH2O)
            + xi_Fe * (mFe + mO)
        )
    )

    x = (
        (1.0 - xi_Fe)
        * ((1.0 - xi_H2O_Per) * mPer + xi_H2O_Per * mH2O - mPer)
        / (mH2O - ((1.0 - xi_Fe) * mPer + xi_Fe * (mFe + mO)))
    )
    print("x =", x)
    print("e =", e)
    m1 = mPer * (1.0 - xi_Fe) + xi_Fe * (mFe + mO)
    m2 = mH2O
    e = eta(xi=x, m1=m1, m2=m2)
    return e


def xi_H2O_Ws(X_H2O_Per=0.0, FeMg=0.0, xiBr=None, lay=1):
    """Computes mole fraction of H2O in Wuestite given a value for mass fraction
    X_H2O_Per of water in Periclase
    """
    xi_Fe = FeMg / (1.0 + FeMg)
    mWs_prime = (mMg + mO) * (1.0 - xi_Fe) + xi_Fe * (mFe + mO)

    # No Wuestite in core and upper mantle
    if lay == 0 or lay == 1 or lay == 3:
        return 0.0

    elif lay == 2:
        return xi(eta=X_H2O_Per, m1=mWs_prime, m2=mH2O)


def xi_H2O_Perov(X_H2O_Perov=0.0, FeMg=0.0, lay=1):
    """Computes mole fraction of H2O in perovskite given a value for masss fraction
    xi_H2O_Perov of water in Perovskite
    """
    xi_Fe = FeMg / (1.0 + FeMg)
    mPerov_prime = mMg * (1 - xi_Fe) + xi_Fe * mFe + 3 * mO + mSi

    # no Perovskite in core and upper mantle
    if lay == 0 or lay == 1 or lay == 3:
        return 0.0

    elif lay == 2:
        return xi(eta=X_H2O_Perov, m1=mPerov_prime, m2=mH2O)


def xi_En(SiMg=None, FeMg=0.0, xi_H2O_Ol=0.0, lay=1):
    """Computes mole fraction of Enstatite at given ratios Si/Mg and Fe/Mg
    for hydration model type 1
    """
    # check consistency if FeMg and SiMg in given mantel
    if FeMg < Fe2Mg_min(SiMg, lay=lay) or FeMg > Fe2Mg_max(SiMg, lay=lay):
        print("WARNING: given Fe/Mg out of range!")
        print(
            "Fe/Mg must be in the interval",
            Fe2Mg_min(SiMg, lay=lay),
            Fe2Mg_max(SiMg, lay=lay),
        )

        return None

    else:
        # no Enstatite in lower mantle or core
        if lay < 3:
            return 0.0

        elif lay == 3:
            xi_Fe = FeMg / (1 + FeMg)
            return 1.0 - 2 * (SiMg * (1 - xi_Fe) - 1) / (
                2 * SiMg * (1.0 - xi_Fe) * xi_H2O_Ol - xi_H2O_Ol - 1.0
            )


# def m_Br(T=None, P=None, ph=None):
#     """Computes mole mass of a periclase molecule according to the phase at
#     given P and T (in the hydrated case it would then be brucite). The phase
#     can also be specified as input in which case P and T will not be used to
#     evaluate the phase. This is useful since in a structure shell, the overall
#     phase is defined for the entire shell even if it crosses a phase transition.
#     """

#     # compute phase region at given PT-point if no phase is given
#     if ph == None:
#         ph = brucite_phase.phaseCheck(T=T, P=P)

#     # dissociated phase
#     if ph == 2:
#         return mMg + mO

#     # hydrated phase
#     else:
#         return mMg + 2 * mO + 2 * mH


def m_Ol(xi_Fe=0.0, **kwargs):
    """Computes mole mass of a hydrated olivine molecule according to the phase
    at given P and T. The phase determines how much water is stored in the
    molecule (on average) and hence the molecular mass. Water content XH2O is
    given in wt fraction (NOT wt%) and iron content in mole fraction (NOT mol%)
    """

    # add corresponding amount of water for one mol of olivine
    # the model treats the water as an average additional weight to each
    # Mg2SiO4 molecule given by the wt%. For X_H2O = 1 there is only water.
    # The effective weight of a Olivine molecule is then infinit which gives
    # the amount of Olivine in a given mass to be zero (M/infinity). For
    # X_H2O = 0. the effective weight of a Olivine molecule is simply mOl
    mOl_prime = mOl * (1.0 - xi_Fe) + xi_Fe * (mOl - 2 * mMg + 2 * mFe)
    return mOl_prime


def m_En(xi_Fe=0.0):
    """Compute effective mass of enstatite for given iron content. Iron content
    xi_Fe is given as a mole fraction (NOT mol%)
    """

    mEn_prime = mEn * (1 - xi_Fe) + xi_Fe * (mEn - 2 * mMg + 2 * mFe)
    return mEn_prime


def m_Ws(xi_Fe=None):
    """Compute mole mass of Wuestite at given Fe content"""
    return (1.0 - xi_Fe) * mMg + xi_Fe * mFe + mO


def m_Perov(xi_Fe=None):
    """Compute mole mass of Perovskite at given Fe content."""
    return (1 - xi_Fe) * mMg + xi_Fe * mFe + mSi + 3 * mO


def abundance_to_ratio(ab, ab_sol):
    return 10 ** (ab + ab_sol)


def N_all(M=1.0, FeMg=0.0, SiMg=None, X_H2O_Ol=0.0, X_H2O_Ws=0.0, lay=1, **kwargs):
    """Computes the total amount of per, ol and Fe in mole for a planet of total
    mass M in m_earth given values for Mg# and Si# and in the case that the Si phases
    are unhydrous (if they are hydrous the total mass would not be known
    exactly at given Mg# and Si# as it would depend on the amount of water
    in the Si phases which in turn depends on the T and P profiles)

    X_H2O is water content in corresponding phase in mass fraction (NOT wt%)

    """

    # check consistency if FeMg and SiMg in given mantel
    if FeMg < Fe2Mg_min(SiMg, lay=lay) or FeMg > Fe2Mg_max(SiMg, lay=lay):
        print("WARNING: given Fe/Mg out of range!")
        print(
            "Fe/Mg must be in the interval",
            Fe2Mg_min(SiMg, lay=lay),
            Fe2Mg_max(SiMg, lay=lay),
        )

        return None

    else:
        xiH2O_Ol = xi_H2O_Ol(X_H2O_Ol=X_H2O_Ol, FeMg=FeMg, lay=lay)
        xiH2O_Ws = xi_H2O_Ws(X_H2O_Per=X_H2O_Ws, FeMg=FeMg, lay=lay)
        xiOl = xi_Ol(SiMg=SiMg, FeMg=FeMg, xi_H2O_Ol=xiH2O_Ol, lay=lay)
        xiEn = 1.0 - xiOl
        xiFe = xi_Fe(SiMg=SiMg, FeMg=FeMg, lay=lay)
        xiWs = xi_Ws(SiMg, FeMg, xi_H2O_Ws=0.0, lay=lay)
        xiPerov = 1.0 - xiWs

        m_enstatite = m_En(xi_Fe=xiFe)
        m_olivine = m_Ol(xi_Fe=xiFe)
        m_wuestite = m_Ws(xi_Fe=xiFe)
        m_perovskite = m_Perov(xi_Fe=xiFe)
        print("xi_Ol =", xiOl)

        # composition is (Mg,Fe)O + (Mg,Fe)SiO3
        if lay == 1:
            N = M / (
                xiPerov * m_perovskite
                + xiWs * (1 - xiH2O_Ws) * m_wuestite
                + xiH2O_Ws * mH2O
            )
            NMg = N * (1 - xiFe)
            NFe = N * xiFe
            NSi = N * xiPerov
            NH2O = N * xiWs * xiH2O_Ws

        # composition is (Mg,Fe)2SiO4 + (Mg,Fe)2Si2O6
        elif lay == 2:

            N = M / (
                xiEn * m_enstatite + xiOl * (1 - xiH2O_Ol) * m_olivine + xiH2O_Ol * mH2O
            )

            NMg = N * 2 * (1 - xiFe) * (1 - xiOl * xiH2O_Ol)
            NFe = N * 2 * xiFe * (1 - xiOl * xiH2O_Ol)
            NSi = N * (2 - xiOl * (1 + xiH2O_Ol))
            NH2O = N * xiOl * xiH2O_Ol

        return N, NMg, NFe, NSi, NH2O


def N_tot(M=None, SiMg=None, lay=1, X_H2O_Ol=0.0, X_H2O_En=0.0, FeMg=0.0, **kwargs):
    """Computes total number of moles in a shell for the hydration model.
    X_H2O_ol is the water content in Mg2SiO4 in wt%
    """
    # check consistency if FeMg and SiMg in given mantel
    if FeMg < Fe2Mg_min(SiMg, lay=lay) or FeMg > Fe2Mg_max(SiMg, lay=lay):
        print("WARNING: given Fe/Mg out of range!")
        print(
            "Fe/Mg must be in the interval",
            Fe2Mg_min(SiMg, lay=lay),
            Fe2Mg_max(SiMg, lay=lay),
        )

        return None

    else:
        xiH2O_Ol = xi_H2O_Ol(X_H2O=X_H2O_Ol, FeMg=FeMg, lay=lay)
        xiOl = xi_Ol(SiMg=SiMg, FeMg=FeMg, xi_H2O_Ol=xiH2O_Ol, lay=lay)
        xiEn = 1.0 - xiOl
        xiFe = xi_Fe(SiMg=SiMg, FeMg=FeMg, lay=lay)
        xiWs = xi_Ws(SiMg, FeMg, xi_H2O_Ws=0.0, lay=lay)
        xiPerov = 1.0 - xiWs
        """
        print ('xi_Fe =', xiFe)
        print ('xi_ol =', xiOl)
        print ('xi_en =', xiEn)
        print ('xi_ws =', xiWs)
        print ('xi_perov =', xiPerov)
        print ('xi_H2O =', xiH2O_Ol)
        """

        m_enstatite = m_En(xi_Fe=xiFe)
        m_olivine = m_Ol(xi_Fe=xiFe)
        m_wuestite = m_Ws(xi_Fe=xiFe)
        m_perovskite = m_Perov(xi_Fe=xiFe)
        """
        print ('m_olivine =', m_olivine)
        print ('m_enstatite =', m_enstatite)
        print ('m_perovskite =', m_perovskite)
        print ('m_wuestite =', m_wuestite)
        """
        # print ('fractions =', xi1, xi2)
        # print ('m_per =', m_per(T=T, P=P, ph=ph_per))
        # print ('m_mean =', xi1*m_per(T=T, P=P, ph=ph_per) + xi2*m_ol(T=T, P=P, ph=ph_ol))
        if lay == 0:
            return M / mFe

        # the transition from lower to upper mantle is given by the phase
        # transition of Mg2SiO4 -> MgSiO3 + MgO
        # in the model, the lower mantle contains MgO + Mg(OH)2 + MgSiO3
        elif lay == 1:
            return M / (xiWs * m_wuestite + xiPerov * m_perovskite)

        # in the model, the upper mantle contains Mg(OH)2 + Mg2SiO4
        # Mg2SiO4 can contain water. This is accounted for by adjusting the mole mass
        # of Mg2SiO2. One mole of Mg2SiO2 will be heavier if part of it contains
        # some water in addition. Therefore, at a given mass M the total number of
        # particles will be larger in the anhydrous case as the mean particle mass
        # is smaller

        elif lay == 2:
            return M / (
                xiEn * m_enstatite + xiOl * (1 - xiH2O_Ol) * m_olivine + xiH2O_Ol * mH2O
            )


def N_Mg(M=None, SiMg=None, lay=1, X_H2O_Ol=0.0, X_H2O_En=0.0, FeMg=0.0, **kwargs):
    """Computes number of moles of magnesium in mass M containing periclase
    and olivine (hydrous or unhydrous). The molar fractions for both constitutents
    are defined via the Mg# and Si#. X_H2O_ol is the water content in Mg2SiO4
    in weight fraction (NOT wt%)
    """
    # check consistency if FeMg and SiMg in given mantel
    if FeMg < Fe2Mg_min(SiMg, lay=lay) or FeMg > Fe2Mg_max(SiMg, lay=lay):
        print("WARNING: given Fe/Mg out of range!")
        print(
            "Fe/Mg must be in the interval",
            Fe2Mg_min(SiMg, lay=lay),
            Fe2Mg_max(SiMg, lay=lay),
        )

        return None

    else:
        xiH2O_Ol = xi_H2O_Ol(X_H2O=X_H2O_Ol, FeMg=FeMg, lay=lay)
        xiH2O_Ws = 0.0
        xiOl = xi_Ol(SiMg=SiMg, FeMg=FeMg, xi_H2O_Ol=xiH2O_Ol, lay=lay)
        xiEn = 1.0 - xiOl
        xiFe = xi_Fe(SiMg=SiMg, FeMg=FeMg, lay=lay)
        xiWs = xi_Ws(SiMg, FeMg, xi_H2O_Ws=0.0, lay=lay)
        xiPerov = 1.0 - xiWs
        """
        print ('xi_Fe =', xiFe)
        print ('xi_ol =', xiOl)
        print ('xi_en =', xiEn)
        print ('xi_ws =', xiWs)
        print ('xi_perov =', xiPerov)
        print ('xi_H2O =', xiH2O_Ol)
        """

        m_enstatite = m_En(xi_Fe=xiFe)
        m_olivine = m_Ol(xi_Fe=xiFe)
        m_wuestite = m_Ws(xi_Fe=xiFe)
        m_perovskite = m_Perov(xi_Fe=xiFe)
        """
        print ('m_olivine =', m_olivine)
        print ('m_enstatite =', m_enstatite)
        print ('m_perovskite =', m_perovskite)
        print ('m_wuestite =', m_wuestite)
        """
        # the transition from lower to upper mantle is given by the phase
        # transition of Mg2SiO4 -> MgSiO3 + MgO
        # in the model, the lower mantle contains MgO + Mg(OH)2 + MgSiO3
        if lay == 1:
            return (
                M
                / (xiWs * m_wuestite + xiPerov * m_perovskite)
                * (1 - xiFe)
                * (1.0 - xiWs * xiH2O_Ws)
            )

        # in the model, the upper mantle contains Mg(OH)2 + Mg2SiO4
        # Mg2SiO4 can contain water. This is accounted for by adjusting the mole mass
        # of Mg2SiO2. One mole of Mg2SiO2 will be heavier if part of it contains
        # some water in addition. Therefore, at a given mass M the total number of
        # particles will be larger in the anhydrous case as the mean particle mass
        # is smaller

        elif lay == 2:
            return (
                M
                / (
                    xiEn * m_enstatite
                    + xiOl * (1 - xiH2O_Ol) * m_olivine
                    + xiH2O_Ol * mH2O
                )
                * 2
                * (1 - xiFe)
                * (1 - xiOl * xiH2O_Ol)
            )


# def plot_abundance_change(SiMg=None, FeMg=None, lay=1):
#     """Visualize how the relative abundances xi_Ol vs. xi_En changes as a
#     function of the hydration level. This gives the range within which the
#     abundances have to be updated in each shell.
#     """

#     fig, ax = plt.subplots()

#     # Create range of hydration in mol% (not physical!!!)
#     xiH2O = np.logspace(-3, -1)
#     FeMg_list = np.linspace(0.0, 0.5, 6)

#     for FeMg in FeMg_list:
#         xiOl_dry = xi_Ol(SiMg=SiMg, FeMg=FeMg, xi_H2O_Ol=0.0, lay=lay)
#         xiFe = xi_Fe(FeMg=FeMg, SiMg=SiMg)
#         print(xiFe)
#         SiMg_list = (2.0 - xiOl_dry * (1.0 + xiH2O)) / (
#             2 * (1 - xiFe) * (1.0 - xiOl_dry * xiH2O)
#         )

#         xiOl = xi_Ol(SiMg=SiMg, FeMg=FeMg, xi_H2O_Ol=xiH2O, lay=lay)

#         ax.semilogy(xiH2O, (SiMg_list - SiMg) / SiMg)


# def plot_molarmass(SiMg=[], xmin=0.0, xmax=0.2):
#     """ """
#     fig, ax = plt.subplots()
#     ax.set_xlim(xmin * 100, xmax * 100)

#     ax.set_xlabel(r"$X_{H_2 O} \ in  \ Olivine \ [wt \%]$")
#     ax.set_ylabel(r"$\rm molar \ mass \ [kg]$")

#     substances = [mH2O, mBr, mPer, mOl]
#     substances_names = [r"$H_2 O$", r"$Mg(OH)_2$", r"$MgO$", r"$Mg_2 Si O_4$"]

#     for i in range(len(substances)):
#         sub = substances[i]
#         name = substances_names[i]
#         ax.plot([xmin * 100, xmax * 100], [sub, sub], color="k", linestyle=":")
#         ax.text(5.0, sub * 1.01, name)

#     x = np.linspace(xmin, xmax, 100)

#     for SM in SiMg:
#         y = N_tot(M=1.0, SiMg=SM, ph_per=2, ph_ol=0, X_H2O_ol=x, lay=2)

#         ax.plot(x * 100, 1 / y, label="Si/Mg = " + str(round(SM, 3)))

#     ax.legend()


# def plot_abundance(MgSi=[]):
#     """ """
#     fig, ax = plt.subplots()
#     ax.set_xlabel(r"$Mg \#$")
#     ax.set_ylabel(r"$Si \#$")

#     x = np.linspace(0.0, 1.0)
#     y = []

#     for MS in range(len(MgSi)):
#         y.append(1.0 / (1.0 + 1.0 / SiMg[MS] * (1.0 / x - 1.0)))

#         ax.plot(x, y[MS], label="Mg/Si =" + str(MgSi[MS]))

#     ax.legend(frameon=False)


def brucite_dissoc(layer, what="out"):
    """Checks the phase for each shell in a Mg(OH)2 layer and extracts the
    total amount of water that will be added as a water layer on top due
    to the Mg(OH)2 -> MgO + H2O dissociation in phase 2. This simple function
    is only applicable to pure Mg(OH)2 layers. Inputs are:

        layer: an array containing the Planet.Shell instances of the layer

        what: specifies the type of water content that is to be computed.
        Options are 'in' (amount of water contained in the hydrated Mg(OH)2
        phase) or 'out' (amount of water contained in the surface ocean due to
        the Mg(OH)2 dissociation).
    """
    mass_in = 0.0
    mass_out = 0.0

    for s in range(len(layer.shells)):
        shell = layer.shells[s]

        # Extract phase of Mg(OH)2 in the shell
        phase = shell.mix.mix[0].phase

        if phase == 2:
            # compute number of mols of MgO in the shell
            MgO = shell.indigenous_mass / (mMg + mO)

            mass_out += MgO * (mO + mH * 2)

        if phase == 0 or phase == 1:
            # compute number of mols of Mg(OH)2 in the shell
            MgO2H2 = shell.indigenous_mass / (mMg + 2 * mO + 2 * mH)

            mass_in += MgO2H2 * (mO + mH * 2)

    if what == "in":
        # avoid spurious results due to small water layers which are below the
        # resolution of the structure integration. Here it is set to a hard limit
        # but in the future this value could be adaptively determined using a
        # structure resolution and layer accuracy for individual planets
        if mass_in / layer.mass < 1.0e-4:
            return 0.0

        else:
            return mass_in

    if what == "out":
        # avoid spurious results due to small water layers which are below the
        # resolution of the structure integration. Here it is set to a hard limit
        # but in the future this value could be adaptively determined using a
        # structure resolution and layer accuracy for individual planets
        if mass_out / layer.mass < 1.0e-4:
            return 0.0

        else:
            return mass_out


# def Mg_number(contents=None, layers=None, X_H2O=None):
#     """Compute Mg# for a constructed planet. Inputs are planet.contents,
#     planet.layers and planet.X_H2O of a constructed Planet.Planet object.
#     """
#     Fe_list = []
#     Mg_list = []

#     X_H2O = X_H2O

#     # gather all layers containing Fe or FeO
#     for l in range(len(layers)):
#         Fe = 0.0
#         Mg = 0.0

#         for s in range(len(layers[l].shells)):
#             # print ('-------------\nprocessing layer', l,':')
#             ll = contents[l][0]
#             xH2O = X_H2O[l][0]

#             xiH2O = xi(xH2O / 100, mMg + mO, mMg + 2 * mO + 2 * mH)

#             # extract total shell mass
#             shellmass = layers[l].shells[s].indigenous_mass

#             # compute number of mol of Fe in this layer
#             if ll == 9:
#                 Fe += shellmass / mFe

#             elif ll == 7:
#                 Fe += shellmass / (mFe + mO)

#             else:
#                 Fe += 0.0

#             # compute number of mol of Mg in this layer
#             if ll == 5:
#                 Mg += shellmass / (mMg + mO + xiH2O * (mO + mH * 2))

#             elif ll == 1:
#                 Mg += shellmass / (mMg * 2 + mSi + mO * 4)

#             elif ll == 11:
#                 T = layers[l].shells[s].temp
#                 P = layers[l].shells[s].pres

#                 phase = bruce.phaseCheck(T=T, P=P)

#                 # if Mg(OH)2 is in phase 2 it is MgO by the assumption that
#                 # all H2O is transported to the top if Mg(OH)2 is dissociated
#                 # to MgO + H2O
#                 if phase == 2:
#                     Mg += shellmass / (mMg + mO)

#                 else:
#                     Mg += shellmass / (mMg + mO * 2 + mH * 2)

#             else:
#                 Mg += 0.0

#         Fe_list.append(Fe)
#         Mg_list.append(Mg)

#         # print ('layer contains', Fe,' mol of Fe')
#         # print ('layer contains', Mg,' mol of Mg')

#     try:
#         return sum(Mg_list) / (sum(Mg_list) + sum(Fe_list))

#     except ZeroDivisionError:
#         return 0.0


def estimate_Mcore(
    M_tot=0.0, Mg_number=Mg_number_solar, Si_number=0.0, modelType=0, **kwargs
):
    """Computes core mass for given composition and total planetary mass
    from the given Mg# and Si#.
    """
    # Only Mg(OH)2 in the mantle
    if modelType == 0:
        return M_tot * mFe / (mMg + mO) * (1.0 / Mg_number - 1.0)

    # Brucite and Olivine in the mantle
    # Note: hydrated Olivine has NOT a constant water content. Therefore
    # the core mass can only be estimated at a given total mass
    elif modelType == 1:
        pass


# def reconstructDensities(T=None, P=None, materials=[], **kwargs):
#     """Compute density contributions of each individual component in <materials>
#     by inversing the mixing law
#     """
#     densities = []
#     for l in range(len(materials)):
#         densities.append(eos.Compute(what="dens", ll=materials[l], P=P, T=T)[0])
#     return densities


# def reconstructdPdrho(T=None, P=None, densities=[], materials=[], **kwargs):
#     """Compute dPdrho contributions of each individual component in <materials>
#     by inversing the mixing law
#     """
#     derivatives = []
#     for l in range(len(materials)):
#         derivatives.append(eos.dPdrho(ll=materials[l], P=P, T=T, d=densities[l]))
#     return derivatives


# def gradients(
#     r=None,
#     y=[],
#     gamma=1.0,
#     tempType=0,
#     fractions=[],
#     materials=[],
#     oldgrad=[],
#     rhoType="integrate",
#     **kwargs,
# ):
#     """This function computes all the relevant gradients for the RK solver"""
#     P, m, T, d = y

#     # normally the pressure derivative is updated in each RK substep
#     # this induces an enormeous amount of computational costs but is
#     # crucial as keeping it constant over the RK step induces non-negligible
#     # errors on the P, T, m and rho evolution of the planet

#     # compute densities and pressure derivatives of all materials
#     # densities = reconstructDensities(T=T, P=P, materials=materials)
#     # derivatives = reconstructdPdrho(T=T, P=P, densities=densities,\
#     #                              materials = materials)
#     # print ('T/P/d=', T, P, d)
#     derivatives = [
#         eos.dPdrho(T=T, P=P, ll=materials[i], table=False)
#         for i in range(len(materials))
#     ]
#     # derivatives = [eosfort.interpolate(x=T, y=P, ll=materials[i], params=[5],
#     #                                  nparams=1)
#     # for i in range(len(materials))]
#     # derivatives = [tab.interpolate(param=4, x=T, y=P, ll=0)]
#     # print ('dPdrho individual=', derivatives)
#     # compute mean pressure derivative of the mixture
#     dPdrho = sum(derivatives[i] * fractions[i] for i in range(len(materials)))
#     # K1 = sum([fractions[i]/densities[i] for i in range(len(densities))])**2
#     # K2 = sum([fractions[i]/densities[i]**2 for i in range(len(densities))])
#     # K3 = sum([1./derivatives[i] for i in range(len(densities))])
#     # dPdrho2 = K1/K2*1./K3
#     # compute the radial gradients of the structure parameters
#     dPdr = -G * m * d / r**2
#     dmdr = 4.0 * np.pi * r**2 * d

#     if tempType == 0:
#         dTdr = 0.0

#     elif tempType == 1:
#         dTdr = dPdr * gamma * T / (d * dPdrho)

#     if rhoType == "constant":
#         drhodr = 0.0

#     else:
#         drhodr = dPdr / dPdrho

#     return [dPdr, dmdr, dTdr, drhodr]


class FreeEnergy:
    def __init__(self, potential, potential_type, molar_mass):
        self.potential_type = potential_type
        self.potential = potential
        self.molar_mass = molar_mass

    def compute(self, T=None, P=None, V=None, **kwargs):
        if self.potential_type == "helmholtz":
            # Compute potential
            A = self.potential(T=T, V=V, **kwargs)

            # Compute derivatives
            dAdT_V = ftool.der1(self.potential, T, which="T", V=V, **kwargs)
            dAdV_T = ftool.der1(self.potential, V, which="V", T=T, **kwargs)

            # Compute second derivatives
            d2AdT2_V = ftool.der2(self.potential, T, which="T", V=V, **kwargs)
            d2AdV2_T = ftool.der2(self.potential, V, which="V", T=T, **kwargs)
            d2AdVdT = ftool.dermix(self.potential, V, T, arg1="V", arg2="T", **kwargs)
            from picse.materials.equations_of_state.Wagle2019EOS import P_corr

            self.temperature = T
            self.molar_volume = V
            self.density = self.molar_mass / self.molar_volume  # g / cm^3

            # Pressure needs to be defined seperately
            # This is currently only for Wagle 2019
            def pres(V=None, T=None):
                return -ftool.der1(
                    self.potential, V, which="V", T=T, **kwargs
                ) + P_corr(V)

            self.pressure = pres(V=V, T=T)  # GPa
            self.entropy = -dAdT_V  # kJ / mol / K
            self.enthalpy = A - T * dAdT_V - V * dAdV_T
            self.internal_energy = A - T * dAdT_V
            self.heat_capacity_V = -T * d2AdT2_V  # kJ / mol / K
            self.bulk_modulus_T = -V * ftool.der1(pres, V, which="V", T=T)
            self.thermal_expansion = (
                ftool.der1(pres, T, which="T", V=V) / self.bulk_modulus_T
            )
            self.gamma = (
                self.thermal_expansion
                * self.bulk_modulus_T
                * self.molar_volume
                / (self.heat_capacity_V)
            )
            self.heat_capacity_P = self.heat_capacity_V * (
                1.0 + self.thermal_expansion * self.gamma * self.temperature
            )
            self.bulk_modulus_S = (
                1 + self.thermal_expansion * self.gamma * self.temperature
            ) * self.bulk_modulus_T

            self.sound_speed = np.sqrt(self.bulk_modulus_S / self.density)
            self.helmholtz = A
            self.gibbs = self.helmholtz + self.molar_volume * self.pressure

    def plot_curves(self):
        pass

    def plot_maps(
        self, res=[3, 3], y_range=[3.0, 8.0], x_range=[2000, 10000], log=[False, False],
    **kwargs):
        if log[0]:
            x = np.logspace(np.log10(x_range[0]), np.log10(x_range[1]), 2 ** res[0])

        else:
            x = np.linspace(x_range[0], x_range[1], 2 ** res[0])

        if log[1]:
            y = np.logspace(np.log10(y_range[0]), np.log10(y_range[1]), 2 ** res[0])

        else:
            y = np.linspace(y_range[0], y_range[1], 2 ** res[0])

        dat = np.empty([3, 2, 2 ** res[0], 2 ** res[1]])
        labels = [
            ["Pressure (GPa)", "Density (g/cm^3)"],
            ["Thermal expansion (1/K)", "Isoch. heat (kJ / mol / K)"],
            ["Internal energy (kJ / mol)", "Entropy (kJ / mol / K)"],
        ]
        for i in range(len(x)):
            for j in range(len(y)):
                if self.potential_type == "helmholtz":
                    self.compute(T=x[i], V=y[j], **kwargs)
                elif self.potential_type == "gibbs":
                    self.compute(T=x[i], P=y[j], **kwargs)

                dat[0][0][i][j] = self.pressure
                dat[0][1][i][j] = self.density
                dat[1][0][i][j] = self.thermal_expansion
                dat[1][1][i][j] = self.heat_capacity_V
                dat[2][0][i][j] = self.internal_energy
                dat[2][1][i][j] = self.entropy

        fig, ax = plt.subplots(len(dat), len(dat[0]), figsize=(10, 9))
        for i in range(len(ax)):
            for j in range(len(ax[i])):
                im = ax[i][j].imshow(
                    dat[i][j].T, origin="lower", aspect="equal", extent=[0, 1, 0, 1]
                )
                fig.colorbar(im, ax=ax[i][j], format="%.2e", label=labels[i][j])
                if log[0]:
                    ax[i][j].set_xscale("log")
                    ax[i][j].xaxis.set_major_formatter(plt.FormatStrFormatter("%d"))
                if log[1]:
                    ax[i][j].set_yscale("log")
                    ax[i][j].yaxis.set_major_formatter(plt.FormatStrFormatter("%.2f"))
                ax[i][j].set_xlabel("Temperature (K)")
                ax[i][j].set_ylabel("Volume (cm^3/mol)")
                ax[i][j].set_xticks(np.linspace(0, 1, 3))
                ax[i][j].set_yticks(np.linspace(0, 1, 3))
                ax[i][j].set_xticklabels(
                    ["{:.0f}".format(x_tick) for x_tick in np.linspace(x[0], x[-1], 3)]
                )
                ax[i][j].set_yticklabels(
                    ["{:.2f}".format(y_tick) for y_tick in np.linspace(y[0], y[-1], 3)]
                )

        fig.savefig("eos.pdf", format="pdf", bbox_inches="tight")


class Unit:
    def __init__(
        self,
        ll=None,
        pres=None,
        temp=None,
        dens=None,
        Fe_number=0.0,
        saturation=False,
        **kwargs,
    ):

        self.pres = pres
        self.temp = temp
        self.dens = dens
        self.ll = ll  # material id
        self.material = material_list[ll]
        self.Fe_number = Fe_number
        # self.FeMg = Fe_number / (100.0 - Fe_number)
        self.saturation = saturation

        self.phase = 0
        self.whichEOS = EOS_type[ll]

        # saturated Olivine is treated as an individual material taking into
        # account hydration and iron content
        if ll == 1 and saturation:
            self.ll = 12

        if ll == 0 and self.X_H2O > 0.0:
            pass

        # introduce variable that can enforce a bisection step upon structure
        # integration if spurious behaviour or invalid parameter values are
        # detected (e.g. high density follow low density, negative pressure,
        # mass, density or temoerature etc.)
        self.force_bisection = False
        self.K_isoth = None
        self.dPdrho = None
        self.x_H2O = None

    def print(self, digits=4, level=0):
        """Prints out selection of basic properties of the material unit for
        more convenient handling and debugging purposes.
        """
        which = self.whichEOS

        try:
            d = round(self.dens, digits)

        except TypeError:
            d = self.dens

        try:
            p = round(self.pres * 1.0e-9, digits)

        except TypeError:
            p = self.pres

        try:
            t = round(self.temp, digits)

        except TypeError:
            t = self.temp

        try:
            dp = round(self.dPdrho * 1.0e-9, digits)

        except TypeError:
            dp = self.dPdrho

        try:
            k = round(self.K_isoth * 1.0e-9, digits)

        except TypeError:
            k = self.K_isoth

        formatstr = "{:." + str(digits) + "E}"

        lines = [
            ["material:", self.material],
            ["phase:", self.phase],
            ["hydration [wt%]:", round(self.X_H2O * 100, digits)],
            ["saturation:", str(self.saturation)],
            ["EOS:", EOSstring_list[which]],
            ["density [kg m-3]:", d],
            ["pressure [GPa]", formatstr.format(Decimal(str(p)))],
            ["temperature [K]:", t],
            ["dP/drho [GPa m3/kg]:", dp],
            ["K_isoth [GPa]:", k],
        ]

        for i in range(len(lines)):
            if i == 0:
                print("component specifications:\n")

            elif i == 5:
                print("\nthermodynamic properties:\n")

            line = lines[i]
            print("{:<20} {:>0}".format(line[0], line[1]))

        if level == 1:
            pass
            # print(
            #     "\nK_0   [GPa]  :",
            #     k0,
            #     "\nK_0´ :",
            #     k0prime,
            #     "\nrho_0 [kg/m³]:",
            #     d0,
            #     "\nrho_T0[kg/m³]:",
            #     dT0,
            # )

    def compute(self, d=None, T=None, P=None, phase=None, eos_table=False, **kwargs):
        """
        Here the material paremeters are computed. At least two of the parameters
        d, T, and P need to be passed. The phase region in which the EoS is to be
        evaluated can be specified. If it is not, the phase region will be determined
        from the specified conditions.

        Parameters:
        d (float, optional): Density in kg/m³. Defaults to None.
        T (float, optional): Temperature in K. Defaults to None.
        P (float, optional): Pressure in Pa. Defaults to None.
        phase (int, optional): Phase region. Defaults to None.
        eos_tables (bool, optional): Enable use of EoS tables. Defaults to False.
        """

        if not eos_table is False:
            raise NotImplementedError("This option is not available yet.")

        if d == None:
            dens = self.dens
        else:
            dens = d

        if P == None:
            pres = self.pres
        else:
            pres = P
            self.pres = P

        if T == None:
            temp = self.temp
        else:
            temp = T
            self.temp = T

        dPdrho = self.dPdrho
        K_isoth = self.K_isoth

        if not phase == None:
            self.phase = phase

        # check if temperature and pressure are given, then compute
        # corresponding density and pressure derivative in one go

        if self.eos_table:
            dens, dPdrho, alpha, phase = eosfort.interpolate(
                x=temp, y=pres, params=[3, 5, 6, 10], ll=self.ll, nparams=4
            )

            # The phases are characterized by integer numbers. In the tables
            # they are however stored as floats and are interpolated as all
            # the other parameters. If the interpolation points spread
            # across a phase boundary, the point at which the interpolation
            # is carried out is allocated to phase region which is closer
            # to it in the PT-plane. This is approximately achieved by
            # interpolating the phase as a float and then convert it to int
            phase = int(phase)

        else:
            # print ('in =', self.ll, self.Fe_number, self.saturation, self.phase, temp, pres)
            dens, T, P, dTdP_S, dPdrho, phase, X_H2O, alpha, xi_Al = eos.compute(
                what="all",
                ll=self.ll,
                T=temp,
                P=pres,
                Fe_number=self.Fe_number,
                saturation=self.saturation,
                phase=self.phase,
            )

        # Compute water saturation content in (Mg,Fe)2SiO4
        # NOTE: saturated Olivine is treated as a individual material with
        # material code 12
        if self.ll > 11:
            if self.saturation:
                # Convert water content into weight fraction
                X_H2O = hydration.X_H2O_sat(P=self.pres, T=self.temp) * 0.01

        # for Brucite the water content is constant
        elif self.ll == 11:
            phase = phaseCheck.getPhase(ll=self.ll, T=self.temp, P=self.pres)
            if phase == 2:
                self.saturation = False
                X_H2O = 0.0

            else:
                self.saturation = True
                X_H2O = 0.3089

        elif self.ll == 6:
            if phase == 0:
                self.saturation = False
                X_H2O = 0.0

            elif phase == 1:
                self.saturation = True
                X_H2O = 0.03

        # print (dens, dPdrho)
        K_isoth = dPdrho * dens

        # update material properties from eos outputs
        self.K_isoth = K_isoth

        try:
            self.phase = int(phase)

        except TypeError:
            self.phase = phase

        except ValueError:
            self.phase = phase

        self.dens = dens
        self.pres = pres
        self.temp = temp
        self.alpha = alpha
        self.dPdrho = dPdrho
        self.x_H2O = X_H2O


class Mixture:
    """This is a subclass of the 'Material' routine which accounts for
    multiple component material cells. Each component in the material is
    represented by a 'Unit' instance and associated to a certain fraction
    given of a component that is present in the unit cell as input to the class.
    If no fractions are specified, the unit cell is composed of the same amount
    of each material.

    Possible inputs:

        contents (kwarg, type=int, default=[]):
            a python list containing the material id's (integers) that point to
            the associated EOS that has to be used to treat this material.

        fractions (kwarg, type=list, default=[]):
            a python list containing the fractions for the materials specified
            in the contents list. Note, that there has to be one fraction for
            each material passed to the contents list and they have to add up
            to unity. If one of those conditions is not met, an error message
            will be promted.

        T (kwarg, type=float, default=300):
            Temperature of the mixture in the unit cell in K

        P (kwarg, type=float, default=1.0e5):
            Pressure of the mixture in the unit cell in Pa
    """

    def __init__(
        self,
        contents=[],
        fractions=[],
        temp=None,
        pres=None,
        dens=None,
        Fe_number=[],
        X_H2O=[],
        saturation=[],
        eos_table=False,
        **kwargs,
    ):

        self.eos_table = eos_table
        self.contents = contents
        self.fractions = fractions
        self.materials = [material_list[ll] for ll in self.contents]
        self.mix = []
        self.Fe_number = Fe_number
        self.X_H2O = X_H2O
        self.saturation = saturation
        self.pres = pres
        self.temp = temp
        self.dens = dens
        self.densities = (None,)
        self.dPdrho = (None,)
        self.K_isoth = (None,)
        self.alphas = None
        self.force_bisection = False

        # Ensure fractions are normalized to one
        fractions[-1] = 1 - sum(fractions[0:-1])

        if fractions[-1] < 0:
            raise ValueError("Invalid mole fractions provided.")

        # if no fractions have been specified, distribute the components evenly
        # over the mixture
        if len(fractions) == 0 and not len(contents) == 0:
            # print ('setting up uniform fractions')
            frac = 1.0 / len(self.contents)
            self.fractions = [frac for i in self.contents]

        # if no iron or water contents for the individual materials have been
        # specified, set them to zero for all the materials
        if len(Fe_number) == 0:
            self.Fe_number = [0.0 for i in self.contents]

        if len(X_H2O) == 0:
            self.X_H2O = [0.0 for i in self.contents]

        if len(saturation) == 0:
            self.saturation = [False for i in self.contents]

        for l in range(len(self.contents)):
            if self.saturation[l] == True:
                self.X_H2O[l] = 1.0

        self.update_weight_fractions()

    def update_weight_fractions(self):
        # Compute mass fractions
        self.weight_fractions = []
        m_tilde = 0.0
        for l in range(len(self.contents)):
            m_tilde += self.fractions[l] * molar_mass_list[self.contents[l]]

        for l in range(len(self.contents)):
            ll = self.contents[l]
            self.weight_fractions.append(
                self.fractions[l] * molar_mass_list[ll] / m_tilde
            )

    # def plot(
    #     self,
    #     temps=[500, 1000, 1500, 2000, 2500],
    #     start=5,
    #     end=12,
    #     N=25,
    #     log=True,
    #     **kwargs,
    # ):
    #     """Computes isotherms between 10**start and 10**end for all temperatures
    #     given in temps for the given mixture and plots rho(P) for each T
    #     """

    #     dens = []

    #     if log:
    #         pres = np.logspace(start, end, N)

    #     else:
    #         pres = np.linspace(start, end, N)

    #     for i in range(len(temps)):
    #         dens.append([])
    #         for j in range(len(pres)):
    #             self.Update(T=temps[i], P=pres[j])
    #             dens[-1].append(self.dens)

    #     fig, ax = plt.subplots()

    #     for i in range(len(temps)):
    #         if log:
    #             ax.semilogx(pres, dens[i], label=str(temps[i]) + " K")

    #         else:
    #             ax.plot(pres * 1.0e-9, dens[i], label=str(temps[i]) + " K")

    #     ax.legend()

    #     if log:
    #         ax.set_xlabel(r"$\rmP \ [Pa]$")

    #     else:
    #         ax.set_xlabel(r"$\rmP \ [GPa]$")

    #     ax.set_ylabel(r"$\rm\rho \ [kg \ m^{-3}]$")

    #     title_string = ""
    #     for i in range(len(self.materials)):
    #         title_string += str(self.materials[i])
    #         if i < len(self.materials) and len(self.materials) > 1:
    #             title_string += ", "

    #     ax.set_title(title_string)

    def print(self, individual=False, digits=5, **kwargs):

        try:
            d = round(self.dens, digits)

        except TypeError:
            d = self.dens

        try:
            p = round(self.pres * 1.0e-9, digits)

        except TypeError:
            p = self.pres

        try:
            t = round(self.temp, digits)

        except TypeError:
            t = self.temp

        try:
            dp = round(self.dPdrho * 1.0e-9, digits)

        except TypeError:
            dp = self.dPdrho

        try:
            k = round(self.K_isoth * 1.0e-9, digits)

        except TypeError:
            k = self.K_isoth

        formatstr = "{:." + str(digits) + "E}"

        print("\n-----------------------------------")
        print("Material properties of the mixture:")
        print("-----------------------------------")

        mat_str = "["
        frac_str = "["

        for i in range(len(self.fractions)):
            if i < len(self.fractions) - 1:
                add = ", "

            else:
                add = ""

            frac_str += str(round(self.fractions[i], digits))
            mat_str += self.materials[i]
            frac_str += add
            mat_str += add

        mat_str += "]"
        frac_str += "]"

        lines = [
            ["contents:", mat_str],
            ["fractions:", frac_str],
            ["density [kg/m³]:", d],
            ["pressure [GPa]:", formatstr.format(Decimal(str(p)))],
            ["temperature [K]:", t],
            ["bulk modulus [Gpa]:", self.K_isoth * 1.0e-9],
            ["thermal expansion [K⁻¹]:", self.alpha],
            ["dPdrho [GPa m³/kg]:", self.dPdrho],
        ]

        for i in range(len(lines)):

            line = lines[i]
            print("{:<20} {:>0}".format(line[0], line[1]))

        print("-----------------------------------")

        if individual:
            print("\nThe Mixture contains the following components:")
            for m in range(len(self.mix)):
                print("\n-------", "\n#", m + 1, ":", self.mix[m].material, "\n-------")
                self.mix[m].prt(digits=digits, **kwargs)

            if len(self.mix) == 0:
                print("\nNo material unit(s) initiated yet")

    def compute(self, T=None, P=None, phase=None, **kwargs):
        """This method initializes a new material instance for each of the
        compontents in the mixture specified by the parameter 'contents' at
        given temperature and pressure and computes the density for each
        component individually and the resulting overall density of the mixture
        according to a specified mixing rule.

        Parameters:
        T (float, optional): Temperature in K. Defaults to None.
        P (float, optional): Pressure in Pa. Defaults to None.
        phase (int, optional): Phase tag. Defaults to None.
        """
        # in case a pressure and/or temperature value has been passed to the
        # construct method, update these properties for the unit cell
        if P == None:
            pass
        else:
            self.pres = P

        if T == None:
            pass
        else:
            self.temp = T

        # print (self.X_H2O)
        # print (self.contents)
        # construct each component as a Unit object

        self.mix = [
            Unit(
                ll=self.contents[l],
                pres=self.pres,
                temp=self.temp,
                Fe_number=self.Fe_number[l],
                eos_table=self.eos_table,
                saturation=self.saturation[l],
                **kwargs,
            )
            for l in range(len(self.contents))
        ]

        # update material fractions
        for m in range(len(self.mix)):
            self.mix[m].fraction = self.fractions[m]

        self.update_weight_fractions()

        # compute density for different components individually
        for ll in range(len(self.contents)):
            self.mix[ll].compute(T=self.temp, P=self.pres, phase=phase, **kwargs)

            # if a unit detects a problem, the force_bisection call is here
            # passed to the next level (from unit to mixture)
            if self.mix[ll].force_bisection:
                self.force_bisection = True

        # Update water content
        self.X_H2O = [self.mix[ll].x_H2O for ll in range(len(self.contents))]

        # if a unit has detected a problem, do not proceed with the
        # calculations
        if not self.force_bisection:
            # generate density list
            self.densities = [mm.dens for mm in self.mix]
            self.alphas = [self.mix[m].alpha for m in range(len(self.contents))]
            self.dPdrhos = [self.mix[m].dPdrho for m in range(len(self.contents))]

            # compute mean density of the mixture using an adequate mixing rule
            # self.dens = eosfort.rho_mean(densities=self.densities,
            #                    fractions=self.fractions,
            #                   nmat=len(self.fractions))

            # Compute mean properties
            self.update_volumetric_props()
            self.update_mean_volumetric_props()

            # self.dens = 0.0
            # self.dPdrho = 0.0
            # self.alpha = 0.0

            # for m in range(len(self.materials)):
            #     self.dens += self.weight_fractions[m] / self.densities[m]
            #     self.dPdrho += (
            #         self.weight_fractions[m]
            #         / self.mix[m].dPdrho
            #         / self.densities[m] ** 2
            #     )
            #     self.alpha += (
            #         self.weight_fractions[m] / self.densities[m] * self.mix[m].alpha
            #     )

            # self.dens = 1.0 / self.dens

            # self.dPdrho *= self.dens**2
            # self.dPdrho = 1.0 / self.dPdrho

            # # compute mean isothermal bulk modulus
            # self.K_isoth = self.dPdrho * self.dens

            # self.alpha *= self.dens

            """
            self.dens, self.alpha, self.dPdrho = eosfort.all_mean(
                    densities = self.densities, 
                    alphas = self.alphas, 
                    dpdrhos = self.dPdrhos,
                    fractions=self.fractions,
                    nmat = len(self.fractions))
            """

    def update_volumetric_props(self):
        """
        Updates the individual volumetric properties.
        """
        self.densities = [mm.dens for mm in self.mix]
        self.alphas = [self.mix[m].alpha for m in range(len(self.contents))]
        self.dPdrhos = [self.mix[m].dPdrho for m in range(len(self.contents))]

    def update_mean_volumetric_props(self):
        """
        Updates the bulk volumetric properties from the individual properties.
        """
        self.dens = density_mean(self.densities, self.weight_fractions)
        self.alpha = thermal_expansion_mean(
            self.densities, self.alphas, self.weight_fractions, dens=self.dens
        )
        self.dPdrho = dPdrho_mean(
            self.densities, self.dPdrhos, self.weight_fractions, dens=self.dens
        )
        self.K_isoth = self.dPdrho * self.dens

    def update_fractions(self, newfractions):
        """Changes the relative abundance of the individual components at
        fixed P and T and computes new mean parameters
        """
        self.fractions = newfractions
        self.update_mean_volumetric_props()

    def update(self, P=None, T=None, d=None, dPdrho=None, **kwargs):
        """This method updates the material instance of each component of the
        mixture individually and then computes the new mean density in the cell
        without re-initializing any component objects. If no new pressure or
        temperature is passed, nothing will be done. If d and or dPdrho are
        passed the individual d and dPdrho contributions for each material will
        be reconstructed without calling the eos which is more efficient.

        Parameters:
        P (float, optional): Pressure in Pa. Defaults to None.
        T (float, optional): Temperature in K. Defaults to None.
        d (float, optional): Density in kg per cubic meter. Defaults to None.
        dPdrho (float, optional): Density derivative of pressure. Defaults to None.

        """
        # update only if new pressure and|or temperature has been specified
        if T == None and P == None:
            pass

        else:
            if not T == None:
                self.temp = T

            if not P == None:
                self.pres = P

            # update properties of individual components
            for m in range(len(self.mix)):
                self.mix[m].pres = self.pres
                self.mix[m].temp = self.temp

        # compute density for different components individually
        for ll in range(len(self.contents)):
            self.mix[ll].compute(**kwargs)

            # if a unit detects a problem, the force_bisection call is here
            # passed to the next level (from unit to mixture)
            if self.mix[ll].force_bisection:
                self.force_bisection = True

            # Update water content
            self.X_H2O = self.mix[ll].X_H2O

            # update density list
            self.update_volumetric_props()
            self.update_mean_volumetric_props()


class ThermodynamicSystem:
    def __init__(self, mix_props, connectivity=None):
        self.components = [Mixture(**mp) for mp in mix_props]

        # Set up connections between components.
        # Use linear connectivity by default.
        if connectivity is None:
            pass
        else:
            if not len(connectivity) == len(mix_props):
                raise ValueError(
                    "The conncetivity and mixtures properties are inconsistent."
                )
            else:
                self.connectivity = connectivity

    def set_up(self):
        pass

    def compute(self):
        pass

    def update(self):
        pass

    def equilibriate(self):
        pass


class MetalSilicateSystem(ThermodynamicSystem):
    def __init__(self, temp, pres):
        # Mixture properties of the metals and the silicates
        mix_props = [
            {
                "pres": pres,
                "temp": temp,
                "contents": [1, 2, 3],
                "fractions": [0.5, 0.3, 1.0],
            },
            {
                "pres": pres,
                "temp": temp,
                "contents": [1, 2, 3],
                "fractions": [0.4, 0.3, 1.0],
            },
        ]
        ThermodynamicSystem.__init__(mix_props)


# def HydVsMix(temps=[500, 1000, 1500], log=False, start=0.5e9, end=3.0e10, N=25):

#     if log:
#         pres = np.logspace(start, end, N)

#     else:
#         pres = np.linspace(start, end, N)

#     dens1 = np.zeros([len(temps), N])
#     dens2 = np.zeros([len(temps), N])

#     mix1 = Mixture(contents=[12], eos_table=False, saturation=[True])
#     mix2 = Mixture(contents=[12, 0], eos_table=False, saturation=[False, False])
#     mix1.Compute(T=temps[0], P=pres[0])
#     mix2.Compute(T=temps[0], P=pres[0])

#     for i in range(len(temps)):
#         for j in range(len(pres)):
#             t = temps[i]
#             p = pres[j]

#             mix1.Compute(T=t, P=p)
#             print(mix1.mix[0].X_H2O)
#             xi_H2O = xi(eta=mix1.mix[0].X_H2O, m1=mOl, m2=mH2O)

#             mix2.UpdateFractions(newfractions=[1 - xi_H2O, xi_H2O])
#             mix2.Compute(T=t, P=p)

#             dens1[i][j] = mix1.dens
#             dens2[i][j] = mix2.dens

#     plots = plotTools.Plot(
#         col=1,
#         row=2,
#         axis_labels=[
#             [[r"$P \ \rm [GPa]$", r"$\rho \rm \ [kg \ m^{-3}]$"]],
#             [[r"$P \ \rm [GPa]$", r"$\delta \rho \rm \ [\%]$"]],
#         ],
#         sharey=False,
#         sharex=True,
#         majorlocatorx=[[5], [5]],
#         majorlocatory=[[500], [10]],
#         minorlocatorx=[[1], [1]],
#         minorlocatory=[[100], [5]],
#         axis_limits=[[[[0, 30], [2500, 4000]]], [[[0.0, 30], [-30, 0]]]],
#         wspace=0.1,
#         hspace=0.1,
#         axislabelsize=16,
#         figsize=(10, 5),
#     )

#     lwdth = 2
#     plot_list1 = []
#     plot_list2 = []
#     legend_list2 = []
#     for i in range(len(temps)):
#         (pl1,) = plots.ax[0][0].plot(
#             pres * 1.0e-9,
#             dens1[i],
#             linestyle="-",
#             color=((i) / (len(temps) - 1), 0, 0),
#             linewidth=lwdth,
#             label=str(temps[i]) + " K",
#         )
#         (pl2,) = plots.ax[0][0].plot(
#             pres * 1.0e-9,
#             dens2[i],
#             linestyle="--",
#             color=((i) / (len(temps) - 1), 0, 0),
#             linewidth=lwdth,
#         )

#         plots.ax[1][0].plot(
#             pres * 1.0e-9,
#             (dens2[i] - dens1[i]) / dens1[i] * 100,
#             color=((i) / (len(temps) - 1), 0, 0),
#             linewidth=lwdth,
#         )

#         plot_list2.append(pl1)
#         legend_list2.append(str(temps[i]) + " K")

#         if i == 0:
#             plot_list1.append(pl1)
#             plot_list1.append(pl2)

#     legend1 = plots.ax[0][0].legend(
#         plot_list1, ["linear hydration", "linear mixing"], loc=2, fontsize=12
#     )

#     legend2 = plots.ax[0][0].legend(plot_list2, legend_list2, loc=4, fontsize=12)
#     plots.ax[0][0].add_artist(legend1)
#     plots.ax[0][0].add_artist(legend2)
#     plots.fig.align_xlabels(plots.ax[:])
#     plots.fig.align_ylabels(plots.ax[:])

#     plots.fig.savefig(
#         "/mnt/c/Users/os18o068/Documents/PHD/Abbildungen/hyd_vs_mix.pdf",
#         format="pdf",
#         bbox_inches="tight",
#     )
