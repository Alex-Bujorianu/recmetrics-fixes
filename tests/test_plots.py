import unittest
from unittest import mock

import pandas as pd
from recmetrics import plots


class TestPlots(unittest.TestCase):

    def test_long_tail_plot(self):
        pass

    # BUG: Test failing
    @mock.patch("%s.plots.sns" % __name__)
    def test_coverage_plot(self, mock_plt):

        COVERAGE_SCORES = [0.17, 0.25, 0.76]

        MODEL_NAMES = ['Model A', 'Model B', 'Model C']

        plots.coverage_plot(coverage_scores=COVERAGE_SCORES, model_names=MODEL_NAMES)

        # Assert plt.title has been called with expected arg
        # mock_plt.ax.set_title.assert_called_once_with("Catalog Coverage in X")

        # Assert plt.figure got called
        # assert mock_plt.ax.set_title.called
        # self.assertTrue(mock_plt.show.called)
        self.assertTrue(mock_plt.barplot.called)

    @mock.patch("%s.plots.sns" % __name__)
    def test_personalization_plot(self, mock_sns):
        
        SCORES = [0.13, 0.52, 0.36]

        MODEL_NAMES = ["Model A", "Model B", "Model C"]

        plots.personalization_plot(personalization_scores=SCORES,
            model_names=MODEL_NAMES)

        # mock_sns.set_title.assert_called_once_with("Personalization")
        
        self.assertTrue(mock_sns.barplot.called)
    
    @mock.patch("%s.plots.sns" % __name__)
    def test_intra_list_similarity_plot(self, mock_sns):
        
        SCORES = [0.13, 0.52, 0.36]

        MODEL_NAMES = ["Model A", "Model B", "Model C"]

        plots.intra_list_similarity_plot(
            intra_list_similarity_scores=SCORES,
            model_names=MODEL_NAMES
        )

        self.assertTrue(mock_sns.barplot.called)
    
    @mock.patch("%s.plots.plt" % __name__)
    def test_mark_plot(self, mock_plt):
        """
        Test mark_plot function

        This test assumes the plot output is correct
        """

        # GIVEN mark_plot metrics
        test_mark_scores = [[0.17, 0.25, 0.76], [0.2, 0.5, 0.74]]

        test_model_names = ["Model A", "Model B"]

        test_k_range = [1, 2, 3]

        # WHEN plots.mark_plot is run
        plots.mark_plot(
            mark_scores=test_mark_scores,
            model_names=test_model_names,
            k_range=test_k_range
        )

        # THEN plt.show() should be called in the function
        self.assertTrue(mock_plt.show.called)
    
    @mock.patch("%s.plots.sns" % __name__)
    def test_mapk_plot(self, mock_sns):
        """
        Test mapk_plot function

        This test assumes the plot output is correct
        """

        # GIVEN mapk_plot metrics
        test_mapk_scores = [[0.17, 0.25, 0.76], [0.2, 0.5, 0.74]]

        test_model_names = ["Model A", "Model B"]

        test_k_range = [1, 2, 3]

        # WHEN plots.mapk_plot is run
        plots.mapk_plot(mapk_scores=test_mapk_scores,
            model_names=test_model_names,
            k_range=test_k_range)

        # THEN sns.lineplot() should be called in the function
        self.assertTrue(mock_sns.lineplot.called)

    @mock.patch("%s.plots.plt" % __name__)
    def test_class_separation_plot(self, mock_plt):
        """
        Test class_separation_plot function
        
        This test assumes the plot output is correct
        """
        
        # GIVEN test predictions (formatted as a DataFrame)
        test_predictions = [{'predicted': 0.8234533056632546, 'truth': 1.0},
                            {'predicted': 0.38809152841543315, 'truth': 0.0},
                            {'predicted': 0.6884520702843566, 'truth': 1.0},
                            {'predicted': 0.8619420469620636, 'truth': 1.0},
                            {'predicted': 0.4467523400196148, 'truth': 1.0},
                            {'predicted': 0.1866420601469934, 'truth': 0.0},
                            {'predicted': 0.3254255160354242, 'truth': 0.0},
                            {'predicted': 0.7630648787719122, 'truth': 1.0},
                            {'predicted': -0.057428628469647525, 'truth': 0.0},
                            {'predicted': 0.7552402377980721, 'truth': 1.0}]

        test_pred_df = pd.DataFrame(test_predictions)

        # WHEN plots.class_separation_plot is run
        plots.class_separation_plot(test_pred_df, n_bins=45, title="TEST Class Separation Plot")

        # THEN check if plt.show() is called
        self.assertTrue(mock_plt.show.called)

    # BUG: Test failing
    @mock.patch("%s.plots.plt" % __name__)
    def test_roc_plot(self, mock_plt):
        """
        Test roc_plot function

        This test assumes the plot output is correct
        """
        
        # test_actual = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # test_model_probs = [0.2597283722018475,
        #                     -0.40202508916707275,
        #                     -0.554430069501674,
        #                     -0.18743657893643717,
        #                     -0.0703925547410395,
        #                     0.5121336811899964,
        #                     0.22999284284308816,
        #                     -0.20260715473613444,
        #                     0.3165576766309387,
        #                     -0.8612054894655852]
        test_model_probs = [0.25675615862929957, -0.3500402605481892, 0.15462047283444785, -0.048144819632589375, -0.4510045992976353, 1.135931952507712, 1.4963036334971416, 0.9063572632832708, 0.0363931327600891, 0.7933323254700744, 1.6211624410086427, 1.1929177011579082, 1.0703503925181748, 1.3570834620683483, 0.9929086342243878, 0.8070893354680458, 0.5636264228503749, 0.02502729241762336, 1.1537446384105503, 0.7897101257792519, 1.3499695505008096, 1.557654128186544, 0.8064528650065548, 0.9481737883274762, 2.2084120722223375, 0.5166749989387713, 2.1365178742822466, 0.784015169441857, -0.1661370218345174, 0.711697589317327, 1.62387988053605, 0.2505915964588492, 0.28258977878108893, 1.1343170964174987, 0.5673229357282024, 0.7186855975358546, 1.811627818541539, 1.5419576116094615, 0.29619237395158726, 0.9173111081607632, 0.840391974210991, 1.055552891370175, 0.4237489845393724, 0.8185886054538095, 0.5669129093668325, 0.5978555111670991, 0.8294140579707611, 0.8588874087093545, 1.7832693723643547, 1.1691154796408494, 1.4695140074843496, 0.20118514427022993, 0.18162342629310813, 1.2607325155811948, 1.4073475395838173, 1.1421104294621536, 0.5069801098554556, -0.5607036065585306, 0.8269916610939153, 1.41673702708532]

        test_actual = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


        test_model_names = "Test ROC Plot"

        plots.roc_plot(actual=test_actual,
            model_probs=test_model_probs,
            model_names=test_model_names,
            figsize=(10,10))

        self.assertTrue(mock_plt.show.called)

    @mock.patch("%s.plots.plt" % __name__)
    def test_precision_recall_plot(self, mock_plt):

        test_model_probs = [0.25675615862929957, -0.3500402605481892, 0.15462047283444785, -0.048144819632589375, -0.4510045992976353, 1.135931952507712, 1.4963036334971416, 0.9063572632832708, 0.0363931327600891, 0.7933323254700744, 1.6211624410086427, 1.1929177011579082, 1.0703503925181748, 1.3570834620683483, 0.9929086342243878, 0.8070893354680458, 0.5636264228503749, 0.02502729241762336, 1.1537446384105503, 0.7897101257792519, 1.3499695505008096, 1.557654128186544, 0.8064528650065548, 0.9481737883274762, 2.2084120722223375, 0.5166749989387713, 2.1365178742822466, 0.784015169441857, -0.1661370218345174,
                            0.711697589317327, 1.62387988053605, 0.2505915964588492, 0.28258977878108893, 1.1343170964174987, 0.5673229357282024, 0.7186855975358546, 1.811627818541539, 1.5419576116094615, 0.29619237395158726, 0.9173111081607632, 0.840391974210991, 1.055552891370175, 0.4237489845393724, 0.8185886054538095, 0.5669129093668325, 0.5978555111670991, 0.8294140579707611, 0.8588874087093545, 1.7832693723643547, 1.1691154796408494, 1.4695140074843496, 0.20118514427022993, 0.18162342629310813, 1.2607325155811948, 1.4073475395838173, 1.1421104294621536, 0.5069801098554556, -0.5607036065585306, 0.8269916610939153, 1.41673702708532]

        test_actual = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        plots.precision_recall_plot(targs=test_actual, preds=test_model_probs)

        self.assertTrue(mock_plt.show.called)

    def test_make_listy(self):
        
        # test_x = [(0,1,2), [1,2,3]]

        # plots.is_listy(x=test_x)

        # self.assertTrue()
        pass

    def test_is_listy(self):
        pass

    def test_metrics_plot(self):
        pass
